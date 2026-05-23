# AI-Proctored Online Examination System 🎓🤖

An advanced, secure, and intelligent online examination platform built with Flask and Python. This application is designed to conduct objective, subjective, and practical coding tests while ensuring academic integrity through state-of-the-art AI-based proctoring and monitoring.

## 🌟 Key Features

### Authentication & Security
- **DeepFace Biometric Verification:** Students are authenticated via real-time facial recognition against their registered profiles before starting an exam.
- **Secure Login:** Role-based access control for Professors and Students.

### Comprehensive Testing Modules
- **Objective Exams (MCQ):** Upload questions via CSV. Includes optional calculator and negative marking.
- **Subjective Exams:** Long-form answers with detailed evaluations.
- **Practical Exams:** Built-in code compilation/interpretation support for 15+ programming languages (C, C++, Java, Python, Node.js, etc.).

### AI-Based Live Proctoring
- **Face & Gaze Tracking:** Uses OpenCV and Dlib to detect off-screen glancing, multiple faces, or absence from the camera.
- **Window Event Monitoring:** Tracks if the student switches tabs, minimizes the browser, or opens other applications.
- **Live Monitoring Dashboard:** Professors can monitor live streams and view auto-generated logs of suspicious activities.

### Monetization
- **Stripe Integration:** Professors can purchase "Exam Credits" securely via Stripe to host new exams.

## 🛠️ Technology Stack

- **Backend:** Python, Flask, Flask-WTF, Flask-Session
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** MySQL
- **AI/ML Models:** DeepFace, OpenCV, Dlib (Shape Predictor 68 Face Landmarks)
- **Payments:** Stripe API
- **Containerization:** Docker & Docker Compose

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8+
- MySQL Server
- (Optional) Docker and docker-compose
- A valid Stripe API Key
- An SMTP Email Server (e.g., Gmail with App Passwords) for OTP verification

## 🚀 Getting Started

### Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/Project.git
   cd Project
   ```

2. **Create a Virtual Environment & Install Dependencies:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up the Database:**
   Import the provided database schema into your MySQL instance:
   ```bash
   mysql -u root -p < DB/quizappstructure.sql
   ```

4. **Environment Variables:**
   Update the credentials in `app.py` or export them as environment variables:
   ```python
   MYSQL_HOST = 'localhost'
   MYSQL_USER = 'root'
   MYSQL_PASSWORD = 'your_mysql_password'
   MAIL_USERNAME = 'your_email@gmail.com'
   MAIL_PASSWORD = 'your_app_password'
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```
   *The app will run on http://localhost:5000*

### Docker Installation

You can easily spin up the application and database using Docker Compose:
```bash
docker-compose up --build
```

## 👩‍🏫 User Roles

- **Professor:** Can purchase exam credits, create exams, upload questions via CSV, view student logs, and monitor exams live.
- **Student:** Can register (requires photo upload for AI verification), take assigned exams, and view results.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
