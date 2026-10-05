import streamlit as st
import matplotlib.pyplot as plt
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from predict import predict_disease

st.set_page_config(page_title="DNA Disease Classifier", layout="wide")
st.title("🧬 DNA Sequence Disease Classifier")

# Multi-sequence input
sequences = st.text_area(
    "Enter DNA sequences (one per line, only A/T/C/G):"
).splitlines()

# Health metrics
st.subheader("Optional: Enter Health Metrics")
bp_normal = st.number_input("Blood Pressure Normal (%)", 0, 100, 50)
bp_high = st.number_input("Blood Pressure High (%)", 0, 100, 30)
bp_low = st.number_input("Blood Pressure Low (%)", 0, 100, 20)

sugar_normal = st.number_input("Sugar Level Normal (%)", 0, 100, 40)
sugar_high = st.number_input("Sugar Level High (%)", 0, 100, 45)
sugar_low = st.number_input("Sugar Level Low (%)", 0, 100, 15)

# Prediction
if st.button("Predict Disease"):
    results = []
    if not sequences or all(seq.strip() == "" for seq in sequences):
        st.info("No DNA sequences entered. Assuming Healthy ✅")
        results.append("Healthy")
    else:
        for seq in sequences:
            if seq.strip() == "":
                results.append("Healthy")
            else:
                results.append(predict_disease(seq.upper()))
    
    # Display results
    for seq, res in zip(sequences, results):
        st.write(f"Sequence: {seq if seq.strip() != '' else 'Empty'} => Predicted Disease: {res}")

# Pie charts
st.subheader("Patient Health Metrics Pie Charts")
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Blood pressure
bp_data = [bp_normal, bp_high, bp_low]
bp_labels = ['Normal', 'High', 'Low']
ax[0].pie(bp_data, labels=bp_labels, autopct='%1.1f%%', colors=['green','red','yellow'])
ax[0].set_title("Blood Pressure Levels")

# Sugar level
sugar_data = [sugar_normal, sugar_high, sugar_low]
sugar_labels = ['Normal','High','Low']
ax[1].pie(sugar_data, labels=sugar_labels, autopct='%1.1f%%', colors=['green','red','yellow'])
ax[1].set_title("Sugar Levels")

st.pyplot(fig)
