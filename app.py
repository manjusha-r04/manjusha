from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
import uvicorn
import json
from utils import mask_pii

# Load trained model
model = joblib.load("model/email_classifier.pkl")

# FastAPI app
app = FastAPI()

# Request body format
class EmailRequest(BaseModel):
    input_email_body: str

@app.post("/classify_email")
def classify_email(req: EmailRequest):
    input_text = req.input_email_body

    # Step 1: Mask PII
    masked_text, entity_list = mask_pii(input_text)

    # Step 2: Classify masked email
    category = model.predict([masked_text])[0]

    # Step 3: Format JSON response
    return {
        "input_email_body": input_text,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_text,
        "category_of_the_email": category
    }

# Optional for local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
