# AlphaScope API Design

## Analyze Company

POST /analyze

Input:

{
"company": "NVIDIA"
}

Output:

Research Report

---

## Get Report

GET /report/{id}

---

## Chat

POST /chat

Input:

{
"report_id": 1,
"question": "What are NVIDIA's biggest risks?"
}

---

## Compare Companies

POST /compare

Input:

{
"company1": "NVIDIA",
"company2": "AMD"
}

---

## Timeline

GET /timeline/{company}

---

## Similar Companies

GET /similar/{company}
