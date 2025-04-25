🧠 Quiz Game

A simple, fun quiz web application built with **Django** and **Python**.

This project lets users take multiple-choice quizzes, tracks their scores, and includes an admin panel for managing questions and categories.

🚀 Features

- Multiple-choice quiz questions
- Automatic scoring
- Simple and responsive UI
- Django admin panel for managing quizzes
- Session-based score tracking

📦 Technologies Used

- Python 3.8+
- Django 4.x
- HTML5 / CSS3
- SQLite (default for development)

⚙️ Setup Instructions

Follow the steps below to set up and run the project on your local machine.

1. Clone the Repository

```bash
git clone https://github.com/andrerovee/Quiz-Django.git
cd Quiz-Django

2. Create a Virtual Enviroment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Run the Development Server

Visit http://127.0.0.1:8000/ in your browser to start the quiz!

Project Structure

Quiz-Django/
├── quiz/               # Main quiz app
├── static/             # Static files (CSS, JS)
├── templates/          # HTML templates
├── db.sqlite3          # SQLite database
├── manage.py
├── requirements.txt
└── README.md

TODOs!

Add user login and registration

Add difficulty levels

Add timer for each question

Store user scores and leaderboards
