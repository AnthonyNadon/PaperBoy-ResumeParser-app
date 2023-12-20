from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, send_file
from io import BytesIO
import os
import pandas as pd
import spacy
import fitz
import glob
import re
import tempfile


app = Flask(__name__)
app.secret_key = '4Fqr!6&qL'

# Configuration pour le téléchargement de fichiers
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Assurez-vous que le dossier de téléchargement existe
upload_folder_path = os.path.join(app.root_path, UPLOAD_FOLDER)
if not os.path.exists(upload_folder_path):
    os.makedirs(upload_folder_path)

# Charger le modèle spaCy et les motifs de compétences
# Assurez-vous que ces fichiers se trouvent dans le même répertoire que votre script ou ajustez le chemin en conséquence
model_path = os.path.join(app.root_path, 'PaperBoy-model')
skill_pattern_path = os.path.join(app.root_path, 'skill_patterns.jsonl')

nlp = spacy.load(model_path)
ruler_skills = nlp.add_pipe("entity_ruler", name="ruler_skills", after="ner")
ruler_skills.from_disk(skill_pattern_path)

# Fonction pour lire le texte d'un fichier PDF
def read_pdf(file_path):
    doc = fitz.open(file_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

# Fonction pour l'extraction d'entités
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Extraction des numéros de téléphone et des courriels
    phone_numbers = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    for number in phone_numbers:
        entities.append((number, "PHONE_NUMBER"))
    for email in emails:
        entities.append((email, "EMAIL"))
    return entities

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    # Vider le dossier uploads avant de sauvegarder de nouveaux fichiers
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    uploaded_files = request.files.getlist("file")
    for file in uploaded_files:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return redirect(url_for('process_files'))


@app.route('/faq')
def faq():
    return render_template('FAQ.html')


@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/process')
def process_files():
    directory_path = app.config['UPLOAD_FOLDER']
    pdf_files = glob.glob(os.path.join(directory_path, "*.pdf"))
    data = {"ID": [], "Entity": [], "Label": []}

    for file_path in pdf_files:
        try:
            text = read_pdf(file_path)
            entities = extract_entities(text)
            file_id = os.path.splitext(os.path.basename(file_path))[0]
            for entity, label in entities:
                data["ID"].append(file_id)
                data["Entity"].append(entity)
                data["Label"].append(label)
        except Exception as e:
            print(f"Erreur lors du traitement du fichier {file_path}: {e}")

    # Création et transformation du DataFrame
    df = pd.DataFrame(data)
    grouped = df.groupby(['ID', 'Label'])['Entity'].apply(lambda x: ', '.join(set(x))).reset_index()
    pivot_df = grouped.pivot(index='ID', columns='Label', values='Entity').reset_index()

    # Vérifier si les colonnes 'SKILL' et 'SKILLS' existent, sinon les créer avec des valeurs par défaut
    if 'SKILL' not in pivot_df.columns:
        pivot_df['SKILL'] = "NA (should be verified)"
    if 'SKILLS' not in pivot_df.columns:
        pivot_df['SKILLS'] = "NA (should be verified)"
    
    # Gérer la fusion des colonnes et l'ordre des colonnes
    pivot_df['SKILL'] = pivot_df['SKILL'].combine_first(pivot_df.get('SKILLS', pd.Series()))
    if 'SKILLS' in pivot_df:
        pivot_df.drop('SKILLS', axis=1, inplace=True)

    if 'EMAIL ADDRESS' in pivot_df:
        pivot_df['EMAIL'] = pivot_df['EMAIL ADDRESS'].combine_first(pivot_df.get('EMAIL', pd.Series()))
        pivot_df.drop('EMAIL ADDRESS', axis=1, inplace=True)

    # Modification pour regrouper CERTIFICATION, COLLEGE NAME, UNIVERSITY, DEGREE sous EDUCATION
    cols_for_education = ['CERTIFICATION', 'COLLEGE NAME', 'UNIVERSITY', 'DEGREE']
    existing_cols = [col for col in cols_for_education if col in pivot_df.columns]
    pivot_df['EDUCATION'] = pivot_df[existing_cols].apply(
        lambda row: ', '.join(filter(None, [str(v) for v in row if pd.notna(v)])), axis=1)

    # Supprimer les colonnes originales si elles existent dans le DataFrame
    for col in existing_cols:
        pivot_df.drop(col, axis=1, inplace=True)

    # Modification pour regrouper COMPANIES WORKED AT et WORKED AS sous une nouvelle colonne Experience
    cols_for_experience = ['COMPANIES WORKED AT', 'WORKED AS']
    existing_cols_exp = [col for col in cols_for_experience if col in pivot_df.columns]
    pivot_df['Experience'] = pivot_df[existing_cols_exp].apply(
        lambda row: ', '.join(filter(None, [str(v) for v in row if pd.notna(v)])), axis=1)

    # Supprimer les colonnes originales si elles existent dans le DataFrame
    for col in existing_cols_exp:
        if col in pivot_df.columns:
            pivot_df.drop(col, axis=1, inplace=True)

    # Réorganiser les colonnes en fonction des nouvelles spécifications
    desired_order = ['ID', 'NAME', 'PHONE_NUMBER', 'EMAIL', 'EDUCATION', 'Experience', 'SKILL'] + \
                    [col for col in pivot_df.columns if col not in ['ID', 'NAME', 'PHONE_NUMBER', 'EMAIL', 'EDUCATION', 'Experience', 'SKILL']]
    pivot_df = pivot_df[desired_order]

    # Après toutes les manipulations de pivot_df, mais avant de sauvegarder ou d'afficher les résultats
    cols_to_exclude = ['AWARDS', 'LANGUAGE', 'LOCATION', 'YEAR OF GRADUATION']
    pivot_df = pivot_df.drop(columns=[col for col in cols_to_exclude if col in pivot_df.columns], errors='ignore')


     # Création d'un fichier temporaire pour stocker les résultats
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    pivot_df.to_csv(temp_file.name, index=False)

    # Imprimer le chemin du fichier temporaire pour le vérifier
    print("Chemin du fichier temporaire:", temp_file.name)

    # Stocker le chemin du fichier temporaire pour un accès ultérieur
    session['temp_csv_path'] = temp_file.name

    # Rediriger vers la page de chargement
    return redirect(url_for('loading'))




@app.route('/results')
def results():
    temp_csv_path = session.get('temp_csv_path')
    if temp_csv_path and os.path.exists(temp_csv_path):
        df = pd.read_csv(temp_csv_path)
        data = df.to_dict(orient='records')  # Convertit le DataFrame en liste de dictionnaires
        return render_template('resultats.html', data=data)
    else:
        return "Fichier non trouvé", 404





@app.route('/download_file')
def download_file():
    temp_csv_path = session.get('temp_csv_path')
    if temp_csv_path and os.path.exists(temp_csv_path):
        with open(temp_csv_path, 'rb') as f:
            data = f.read()

        bio = BytesIO(data)
        bio.seek(0)

        return send_file(bio, 
                         as_attachment=True, 
                         download_name='PaperBoy_Results.csv',
                         mimetype='text/csv')
    else:
        return "Fichier non trouvé", 404










if __name__ == '__main__':
    app.run(debug=True)
