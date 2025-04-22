# 📧 Email Classification with PII Masking

This project is for classifying support emails while masking sensitive information like names, email IDs, Aadhar numbers, etc.

---

## 🔧 How to Run

1. Clone the repo
```bash
git clone https://github.com/your-username/email-classification-api.git
cd email-classification-api
pip install -r requirements.txt
python models.py
uvicorn app:app --reload
```

---

## 🧪 API Usage

**POST Endpoint:** `/classify_email`

### Example Input:
```json
{
  "input_email_body": "Hi, my name is Riya Sharma. My Aadhar is 1234 5678 9012 and email is riya@example.com"
}
```

### Example Output:
```json
{
  "input_email_body": "Hi, my name is Riya Sharma. My Aadhar is 1234 5678 9012 and email is riya@example.com",
  "list_of_masked_entities": [
    {
      "position": [18, 30],
      "classification": "full_name",
      "entity": "Riya Sharma"
    },
    {
      "position": [47, 61],
      "classification": "aadhar_num",
      "entity": "1234 5678 9012"
    },
    {
      "position": [74, 90],
      "classification": "email",
      "entity": "riya@example.com"
    }
  ],
  "masked_email": "Hi, my name is [full_name]. My Aadhar is [aadhar_num] and email is [email]",
  "category_of_the_email": "Billing Issue"
}
```
---

## 📁 Project Files

- `app.py`: FastAPI API
- `models.py`: Email classification model training
- `utils.py`: PII masking logic
- `requirements.txt`: Project dependencies
- `data/emails.csv`: Email dataset
- `model/email_classifier.pkl`: Trained model
- `README.md`: Project documentation

---

## 👩‍💻 Made by

**Manjusha**  
M.Tech – Cloud Computing  
Intern at Akaike Technologies
