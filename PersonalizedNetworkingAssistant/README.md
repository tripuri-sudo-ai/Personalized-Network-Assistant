# 🤝 Personalized Networking Assistant

## 📌 Overview

The **Personalized Networking Assistant** is an AI-powered web application developed as part of the **SmartBridge Internship Project**.

The application helps users prepare for professional networking events by:

* Detecting important themes from an event description using **DistilBERT**
* Generating networking conversation starters using **GPT-2**
* Verifying topics using the **Wikipedia API**
* Saving conversation history
* Collecting user feedback through a Streamlit interface

---

## 🚀 Features

* AI-powered Event Theme Detection
* Professional Conversation Generation
* Wikipedia Fact Checker
* Conversation History
* Feedback Logger
* FastAPI REST APIs
* Streamlit Web Interface
* Automated API Testing with Pytest

---

## 🛠 Technologies Used

* Python 3.11
* FastAPI
* Streamlit
* Hugging Face Transformers
* DistilBERT
* GPT-2
* Wikipedia API
* PyTorch
* Pytest

---

## 📂 Project Structure

```
PersonalizedNetworkingAssistant/
│
├── backend/
│   ├── services/
│   ├── app.py
│   ├── routes.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── data/
│   ├── history.json
│   └── feedback.json
│
├── tests/
│   └── test_api.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd PersonalizedNetworkingAssistant
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Backend

```bash
python -m uvicorn backend.app:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Running the Frontend

```bash
streamlit run frontend/app.py
```

Application URL:

```
http://localhost:8501
```

---

## 📡 API Endpoints

| Method | Endpoint               | Description               |
| ------ | ---------------------- | ------------------------- |
| GET    | /                      | Health Check              |
| POST   | /analyze-event         | Analyze Event Themes      |
| POST   | /generate-conversation | Generate Conversation     |
| POST   | /fact-check            | Verify Topic              |
| GET    | /history               | View Conversation History |
| POST   | /feedback              | Save User Feedback        |

---

## 🧪 Testing

Run all tests:

```bash
pytest
```

Expected Result:

```
4 passed
```

---

## 📸 Application Features

* Event Theme Detection
* Conversation Generation
* Wikipedia Fact Verification
* Conversation History
* Feedback Collection

---

## 🔮 Future Improvements

* Improve conversation quality using newer language models
* User authentication
* Database integration
* Personalized recommendations
* Export conversation history

---

## 👨‍💻 Developed For

**SmartBridge Internship Project**

Built using **FastAPI**, **Streamlit**, **DistilBERT**, **GPT-2**, and the **Wikipedia API**.
