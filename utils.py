import re

def mask_pii(text):
    entities = []

    # Full Name (basic pattern for names starting with capital letters)
    name_pattern = re.compile(r'\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\b')
    text, entities = _mask_and_store(text, name_pattern, 'full_name', entities)

    # Email
    email_pattern = re.compile(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b')
    text, entities = _mask_and_store(text, email_pattern, 'email', entities)

    # Phone Number
    phone_pattern = re.compile(r'\b[789]\d{9}\b')
    text, entities = _mask_and_store(text, phone_pattern, 'phone_number', entities)

    # DOB - formats: DD/MM/YYYY, DD-MM-YYYY
    dob_pattern = re.compile(r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')
    text, entities = _mask_and_store(text, dob_pattern, 'dob', entities)

    # Aadhar Number (12 digits)
    aadhar_pattern = re.compile(r'\b\d{4}\s\d{4}\s\d{4}\b')
    text, entities = _mask_and_store(text, aadhar_pattern, 'aadhar_num', entities)

    # Credit/Debit Card Number (16 digits)
    card_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    text, entities = _mask_and_store(text, card_pattern, 'credit_debit_no', entities)

    # CVV (3 digits)
    cvv_pattern = re.compile(r'\b\d{3}\b')
    text, entities = _mask_and_store(text, cvv_pattern, 'cvv_no', entities)

    # Expiry (MM/YY or MM/YYYY)
    expiry_pattern = re.compile(r'\b(0[1-9]|1[0-2])[/-](\d{2}|\d{4})\b')
    text, entities = _mask_and_store(text, expiry_pattern, 'expiry_no', entities)

    return text, entities

def _mask_and_store(text, pattern, entity_type, entities):
    for match in pattern.finditer(text):
        start, end = match.span()
        value = match.group()
        text = text[:start] + f'[{entity_type}]' + text[end:]
        entities.append({
            "position": [start, start + len(f'[{entity_type}]')],
            "classification": entity_type,
            "entity": value
        })
    return text, entities
