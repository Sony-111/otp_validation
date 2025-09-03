**OTP Validation System**

A secure web-based application built using Django that enables OTP (One-Time Password) verification for user authentication. This project is designed to provide a simple yet effective mechanism for validating user identity through email/mobile OTPs.

**Features**

User registration and login system

OTP generation and validation for secure access

Expiry time for OTPs to enhance security

Database integration with Django ORM

Responsive interface for desktop and mobile


**Tech Stack**

Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default)

Other Tools: SMTP or third-party email gateway (for OTP delivery)

**Project Structure**

otp-validation/
│
├── otp_app/           # Main Django app
│   ├── models.py      # User & OTP models
│   ├── views.py       # Business logic
│   ├── urls.py        # URL routing
│   └── templates/     # HTML templates
│
├── manage.py          # Django management script
├── settings.py        # Project settings
└── requirements.txt   # Dependencies

**Installation & Usage**
1.Clone the repository
git clone https://github.com/Sony-111/otp-validation.git
cd otp-validation
2.Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3.Install dependencies
pip install -r requirements.txt
4.Run the server
python manage.py runserver

**Future Enhancements**

SMS-based OTP delivery

Two-factor authentication integration

Resend OTP functionality

Dashboard for tracking user logins
