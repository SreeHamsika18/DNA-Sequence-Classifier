
import numpy as np
from sklearn.preprocessing import LabelEncoder

def one_hot_encode(sequence):
    mapping = {'A':[1,0,0,0],'T':[0,1,0,0],'C':[0,0,1,0],'G':[0,0,0,1]}
    return np.array([mapping[char] for char in sequence])

def encode_sequences(sequences):
    max_len = max(len(seq) for seq in sequences)
    encoded = []
    for seq in sequences:
        one_hot = one_hot_encode(seq)
        if len(seq) < max_len:
            padding = np.zeros((max_len - len(seq), 4))
            one_hot = np.vstack((one_hot, padding))
        encoded.append(one_hot.flatten())
    return np.array(encoded)

def encode_labels(labels):
    le = LabelEncoder()
    encoded = le.fit_transform(labels)
    return encoded, le
