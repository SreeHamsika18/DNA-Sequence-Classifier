#  DNA Disease Classifier

A machine learning-based application that analyzes DNA sequences and predicts the associated disease category.

##  Project Overview

The DNA Disease Classifier is a machine learning project designed to classify DNA sequences into different disease categories.

The project performs data preprocessing, model training, and prediction using DNA sequence data. A Streamlit interface is provided to make the prediction process simple and user-friendly.

##  Features

- DNA sequence classification
- Data preprocessing
- Machine learning model training
- Disease prediction
- Label encoding
- Streamlit-based user interface
- Trained model saved for prediction
- Simple and user-friendly application

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Machine Learning
- Git & GitHub

##  Project Structure

```text
DNA-Disease-Classifier/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── train.csv
│   └── train.csv.txt
│
├── models/
│   ├── dna_model.pkl
│   └── label_encoder.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── model.py
│   ├── predict.py
│   └── train.py
│
├── generate_train.py
├── .gitignore
└── README.md