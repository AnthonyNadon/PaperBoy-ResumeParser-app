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

# PaperBoy: Resume Parser with Flask, SpaCy & RoBERTa

## Description
This project is a resume management application that uses advanced artificial intelligence techniques to automate and optimize the process of sorting and analyzing resumes. The application is designed to help human resources professionals efficiently manage a large number of applications by converting unstructured data into structured information using NLP, machine learning models like Spacy and RoBERTa-uncased, as well as Regex for pattern recognition.

## Features
- **Automated Processing**: The application processes resumes in various formats, including PDF and Word.
- **Data Extraction**: Uses NLP techniques to extract relevant information from resumes.
- **Intelligent Analysis**: Employs AI models to evaluate and classify applications.
- **Intuitive User Interface**: Facilitates navigation and access to information by users.
- **Data Security**: Protects candidate information with advanced encryption protocols.

## Prerequisites
- Python 3.8+
- Python Libraries: Spacy, PyTorch (for RoBERTa), Regex
- Database (optional for storing resumes)

## Installation

Follow these steps to install and configure the application:

### 1. Clone the Repository
Clone the GitHub repository to your local machine using:
```bash
git clone https://github.com/AnthonyNadon/PaperBoy-ResumeParser-app.git
```

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




