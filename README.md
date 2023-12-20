# PaperBoy : Gestionnaire de CV sous Flask, SpaCy & RoBERTa
*(English below)*

## Description
Ce projet est une application de gestion de CV qui utilise des techniques avancées d'intelligence artificielle pour automatiser et optimiser le processus de tri et d'analyse des curriculum vitae. L'application est conçue pour aider les professionnels des ressources humaines à gérer efficacement un grand nombre de candidatures, en convertissant des données non structurées en informations structurées grâce à l'utilisation de NLP, de modèles d'apprentissage machine comme Spacy et RoBERTa-uncased, ainsi que de Regex pour la reconnaissance de motifs.

## Fonctionnalités
- **Traitement Automatisé** : L'application traite les CV en divers formats, y compris PDF et Word.
- **Extraction de Données** : Utilise des techniques NLP pour extraire des informations pertinentes des CV.
- **Analyse Intelligente** : Emploie des modèles d'IA pour évaluer et classer les candidatures.
- **Interface Utilisateur Intuitive** : Facilite la navigation et l'accès aux informations par les utilisateurs.
- **Sécurité des Données** : Protège les informations des candidats avec des protocoles de cryptage avancés.

## Prérequis
- Python 3.8+
- Bibliothèques Python : Spacy, PyTorch (pour RoBERTa), Regex
- Base de données (optionnelle pour le stockage des CV)

## Installation

Suivez ces étapes pour installer et configurer l'application :

### 1. Cloner le Dépôt
Clonez le dépôt GitHub sur votre machine locale en utilisant :
```bash
git clone https://github.com/votre_nom_utilisateur/votre_repo.git
```
Remplacez `https://github.com/votre_nom_utilisateur/votre_repo.git` par l'URL de votre dépôt GitHub.

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

## Utilisation
to do




