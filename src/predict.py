
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_preprocessing import encode_sequences
from model import load_model

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(project_root, "models", "dna_model.pkl")
encoder_path = os.path.join(project_root, "models", "label_encoder.pkl")

# If model doesn't exist, create it automatically
if not os.path.exists(model_path) or not os.path.exists(encoder_path):
    from train import *
    print("⚠️ Model or encoder missing. Training a new model...")

model = load_model(model_path)
le = load_model(encoder_path)

def predict_disease(sequence):
    try:
        X = encode_sequences([sequence])
        pred = model.predict(X)
        return le.inverse_transform(pred)[0]
    except:
        return "Healthy"
