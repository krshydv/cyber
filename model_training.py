import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("cicids2017_cleaned.csv")

# Encode labels
label_encoder = LabelEncoder()
df['Attack Type'] = label_encoder.fit_transform(df['Attack Type'])

# Save label encoder
joblib.dump(label_encoder, 'label_encoder.pkl')

# Separate features and label
X = df.drop('Attack Type', axis=1)
y = df['Attack Type']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
joblib.dump(scaler, 'scaler.pkl')

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save trained model
joblib.dump(clf, 'threat_detection_model.pkl')

print("✅ Model, scaler, and label encoder saved.")
