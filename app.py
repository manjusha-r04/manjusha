from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import os
from utils import mask_pii

app = FastAPI()

# Load the trained model
model_path = os.path.join("model", "email_classifier.pkl")
model = joblib.load(model_path)

# Define input structure
class EmailInput(BaseModel):
    input_email_body: str

# Define output structure (optional, for clarity)
@app.post("/classify_email")
async def classify_email(data: EmailInput):
    email_body = data.input_email_body

    # Mask PII
    masked_text, entities = mask_pii(email_body)

    # Predict category
    category = model.predict([email_body])[0]

    return {
        "input_email_body": email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_text,
        "category_of_the_email": category
    }
