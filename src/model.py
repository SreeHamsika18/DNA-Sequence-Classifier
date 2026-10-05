
from sklearn.ensemble import RandomForestClassifier
import pickle

def create_model():
    return RandomForestClassifier(n_estimators=100, random_state=42)

def save_model(model, path):
    with open(path, "wb") as f:
        pickle.dump(model, f)

def load_model(path):
    with open(path, "rb") as f:
        return pickle.load(f)
