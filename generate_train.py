
import pandas as pd
import random
import os

# Create data folder if missing
os.makedirs("data", exist_ok=True)

# Function to generate random DNA sequence
def generate_dna(length=15):
    return ''.join(random.choices(['A','T','C','G'], k=length))

# Number of sequences per class
n = 100

data = []

for _ in range(n):
    data.append([generate_dna(), 'Cancer'])
for _ in range(n):
    data.append([generate_dna(), 'Diabetes'])
for _ in range(n):
    data.append([generate_dna(), 'Heart'])
for _ in range(n):
    data.append([generate_dna(), 'Healthy'])

# Create DataFrame
df = pd.DataFrame(data, columns=['sequence', 'disease'])
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save CSV
df.to_csv('data/train.csv', index=False)
print("✅ train.csv created in data/ folder successfully!")
