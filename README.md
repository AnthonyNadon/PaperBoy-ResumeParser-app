# PaperBoy : Gestionnaire de CV sous Flask, SpaCy & RoBERTa
*(English below)*

## Description
Ce projet est une application de gestion de CV qui utilise des techniques avancées d'intelligence artificielle pour automatiser et optimiser le processus de tri et d'analyse des curriculum vitae. L'application est conçue pour aider les professionnels des ressources humaines à gérer efficacement un grand nombre de candidatures, en convertissant des données non structurées en informations structurées grâce à l'utilisation de NLP, de modèles d'apprentissage machine comme Spacy et RoBERTa, ainsi que de Regex pour la reconnaissance de motifs.

## Fonctionnalités
- **Traitement Automatisé** : L'application traite les CV au format PDF
- **Extraction de Données** : Utilise des techniques NLP pour extraire des informations pertinentes des CV.
- **Analyse Intelligente** : Emploie des modèles d'IA pour classer les candidatures.
- **Interface Utilisateur Intuitive** : Facilite la navigation pour les utilisateurs.

## Prérequis
- Python 3.8+
- Bibliothèques Python nécessaires (requirements.txt) :
  - Flask==3.0.0
  - pandas==1.5.3
  - spacy==3.7.2
  - PyMuPDF==1.23.7
  - regex==2023.8.8
  - transformers==4.31.0
  - spacy-alignments==0.9.1
  - spacy-curated-transformers==0.2.1
  - spacy-legacy==3.0.12
  - spacy-llm==0.6.4
  - spacy-loggers==1.0.5
  - spacy-transformers==1.3.3
- Base de données (optionnelle pour le stockage des CV)

## Installation

Suivez ces étapes pour installer et configurer l'application :

### 1. Cloner le Dépôt
Clonez le dépôt GitHub sur votre machine locale en utilisant, ou tout simplement télécharger le fichier .zip :
```bash
git clone https://github.com/AnthonyNadon/PaperBoy-ResumeParser-app.git
```

### 2. Installer les Dépendances
Dans le répertoire du projet, installez les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

### 3. Télécharger le Modèle
Téléchargez le modèle en cliquant sur le lien suivant :
[Télécharger le modèle](https://drive.google.com/uc?export=download&id=1D3DCtKGzi33YQFQZ7lSANkdcTlzocb3H)

### 4. Placer le Modèle dans le Répertoire Approprié
Après avoir téléchargé le fichier du modèle, placez-le dans le bon répertoire.
```
PaperBoy-ResumeParser-app-main/
├── PaperBoy-model/
```
Décompressez le fichier.

### 5. Lancer l'Application
Enfin, lancez l'application:

```bash
python PaperBoy.py
```


## Utilisation
Après avoir lancé l'application, ouvrez un navigateur et accédez à `http://127.0.0.1:5000` pour interagir avec l'application.

## Résultats de l'Entraînement du Modèle

Le graphique ci-dessous illustre l'évolution de la perte (Loss NER) et de la précision (Accuracy NER) du modèle d'apprentissage automatique au cours des différents batches d'entraînement. Notamment, le modèle a atteint un niveau de précision à 87%, ce qui démontre son efficacité et sa fiabilité dans la tâche de reconnaissance d'entités nommées (NER).

![Graphique de la perte et de la précision](https://i.postimg.cc/cCv0HCM6/8cbdced2-c6ef-4b72-a03a-ae9ff8056b1d.png)


# PaperBoy: Resume Parser with Flask, SpaCy & RoBERTa

## Description
This project is a resume management application that uses advanced artificial intelligence techniques to automate and optimize the process of sorting and analyzing resumes. The application is designed to help human resources professionals efficiently manage a large number of applications by converting unstructured data into structured information using NLP, machine learning models like Spacy and RoBERTa-uncased, as well as Regex for pattern recognition.

## Features
- **Automated Processing**: The application processes resumes in PDF format.
- **Data Extraction**: Uses NLP techniques to extract relevant information from resumes.
- **Intelligent Analysis**: Employs AI models to process and classify applications.
- **Intuitive User Interface**: Facilitates navigation by users.

## Prerequisites
- Python 3.8+
- Required Python Libraries (requirements.txt) :
  - Flask==3.0.0
  - pandas==1.5.3
  - spacy==3.7.2
  - PyMuPDF==1.23.7
  - regex==2023.8.8
  - transformers==4.31.0
  - spacy-alignments==0.9.1
  - spacy-curated-transformers==0.2.1
  - spacy-legacy==3.0.12
  - spacy-llm==0.6.4
  - spacy-loggers==1.0.5
  - spacy-transformers==1.3.3
- Database (optional for storing resumes)

## Installation

Follow these steps to install and configure the application:

### 1. Clone the Repository
Clone the GitHub repository to your local machine using:
```bash
git clone https://github.com/AnthonyNadon/PaperBoy-ResumeParser-app.git
```
or simply download the zip file

### 2. Install Dependencies
In the project directory, install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### 3. Download the Model
Download the model by clicking on the following link:
[Download the model](https://drive.google.com/uc?export=download&id=1D3DCtKGzi33YQFQZ7lSANkdcTlzocb3H)

### 4. Place the Model in the Appropriate Directory
After downloading the model file, place it in the correct directory.
```
PaperBoy-ResumeParser-app-main/
├── PaperBoy-model/
```
Unzip the file.

### 5. Launch the Application
Finally, launch the application:

```bash
python PaperBoy.py
```

## Usage
After launching the application, open a browser and go to `http://127.0.0.1:5000` to interact with the application.

## Model Training Results

The graph below illustrates the evolution of the loss (Loss NER) and the accuracy (Accuracy NER) of the machine learning model over various training batches. Notably, the model achieved a level of 87% accuracy, demonstrating its effectiveness and reliability in the task of Named Entity Recognition (NER).

![Graph of Loss and Accuracy](https://i.postimg.cc/cCv0HCM6/8cbdced2-c6ef-4b72-a03a-ae9ff8056b1d.png)




