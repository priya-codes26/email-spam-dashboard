import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the email dataset
data = pd.read_csv("emails.csv")
print("Starting model training...")
print(data.head())
# Create the spam detection model
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model
model.fit(data["text"], data["label"])

# Save the trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")
print("Model saved as model.pkl")