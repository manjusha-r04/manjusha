import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import os

# Path to dataset (update as needed)
data_path = "data/emails.csv"

if not os.path.exists(data_path):
    raise FileNotFoundError(f"{data_path} not found. Please add your dataset to the 'data' folder.")

# Load dataset
df = pd.read_csv(data_path)

# Check columns
if 'email' not in df.columns or 'category' not in df.columns:
    raise ValueError("Dataset must have 'email' and 'category' columns.")

X = df['email']
y = df['category']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/email_classifier.pkl")

print("✅ Model trained and saved in model/email_classifier.pkl")
