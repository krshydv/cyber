import numpy as np
import joblib

# Load model components
model = joblib.load('threat_detection_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Dummy feature extractor – Replace with actual logic
def extract_features_from_packet(packet):
    # Example placeholder for 78 features (adjust based on your dataset)
    return np.zeros((1, scaler.mean_.shape[0]))

# Prediction pipeline
def predict_threat(features):
    scaled = scaler.transform(features)
    pred = model.predict(scaled)
    label = label_encoder.inverse_transform(pred)
    return label[0]
