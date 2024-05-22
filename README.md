
# MOP Check(Mental Health Obesity and Pcos Check)

## Introduction
MOP is a Django web application designed to provide various healthcare services online. It offers features such as mental disorder prediction, PCOS prediction, obesity prediction, appointment scheduling with doctors, and health report generation. Users can register, complete their profiles, and access the different health services provided by the platform.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kelvin-Wepo/M_O_P-Check-
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at `http://127.0.0.1:8000/`.

## Features
- **User Registration**: Users can register on the platform to access its services.
- **Doctor Registration**: Doctors can register with additional details like phone number, specialization, and hospital details.
- **User and Doctor Login**: Secure login functionality for both users and doctors.
- **Profile Management**: Users can complete their profiles with details like date of birth, gender, height, and weight.
- **Health Prediction**: Predicts mental disorders, PCOS, and obesity based on user-provided information.
- **Appointment Scheduling**: Allows users to fix appointments with doctors.
- **Health Report Generation**: Generates health reports based on the user's health test results.
- **Responsive Design**: The application is designed to be responsive and user-friendly.

## Usage
1. Register on the platform as a user or doctor.
2. Complete your profile with necessary details.
3. Use the various health prediction features provided.
4. Fix appointments with doctors as needed.
5. View your health reports and follow the provided advice.

## Technologies Used
- Django: Web framework for building the application.
- Python: Backend programming language.
- Pandas, NumPy, TensorFlow: Used for data processing and machine learning.
- HTML, CSS, Bootstrap: Frontend technologies for the user interface.
- Postgres: Database management system for storing user and health data.

## Contributors
- [Kelvin Wepo](https://github.com/Kelvin-Wepo)
<!-- - [Contributor Name](https://github.com/contributor_username) -->

## License
This project is licensed under the [MIT License](LICENSE).