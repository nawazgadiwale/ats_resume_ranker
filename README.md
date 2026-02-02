ATS Resume Ranker

An AI-powered web application that analyzes resumes and provides ATS (Applicant Tracking System) insights, including resume scoring, skill matching, and feedback.
Built using Django (REST API), React (Vite), and Machine Learning.

🚀 Features

Resume upload (PDF / DOCX)

ATS score generation

Skill extraction & gap analysis

Real-time analysis feedback

REST API integration

Clean dashboard UI

Modular & scalable architecture

🛠 Tech Stack
Frontend

React (Vite)

JavaScript (ES6+)

Axios

CSS (Modular / Component-based)

Backend

Django

Django REST Framework

Python

Machine Learning

Resume parsing & keyword extraction

NLP-based analysis (TF-IDF / ML model)

Database

SQLite (development)

PostgreSQL (production-ready)

📁 Project Structure
ats_resume_ranker/
├── backend/
│   ├── core/
│   ├── resumes/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   └── Dashboard.css
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ats-resume-ranker.git
cd ats-resume-ranker

2️⃣ Backend Setup (Django)
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Backend runs at:

http://127.0.0.1:8000/

3️⃣ Frontend Setup (React + Vite)
cd frontend
npm install
npm run dev


Frontend runs at:

http://localhost:5173/

🔗 API Endpoint
Method	Endpoint	Description
POST	/resumes/	Upload resume & get ATS analysis
🔐 CORS Configuration

Ensure this is set in Django settings.py:

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

📸 UI Preview

Dashboard includes:

Resume upload card

Real-time analysis loader

ATS score & insights panel

📌 Future Enhancements

Job description matching

Resume improvement suggestions

Downloadable ATS report

Admin dashboard

Authentication & user profiles

Cloud deployment (AWS / Azure)

👨‍💻 Author

Adnan Patel
Computer Science Engineer
Backend & Full Stack Developer

📄 License

This project is for educational and demonstration purposes.
