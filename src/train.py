import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_preprocessing import encode_sequences, encode_labels
from model import create_model, save_model

# Paths
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data", "train.csv")
models_path = os.path.join(project_root, "models")
os.makedirs(models_path, exist_ok=True)
model_file = os.path.join(models_path, "dna_model.pkl")
encoder_file = os.path.join(models_path, "label_encoder.pkl")

# Load dataset
data = pd.read_csv(data_path)
X = encode_sequences(data['sequence'])
y, le = encode_labels(data['disease'])

# Train model
model = create_model()
model.fit(X, y)

# Save model and encoder
save_model(model, model_file)
save_model(le, encoder_file)

print("✅ Model trained and saved successfully!")
