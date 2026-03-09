# Setup basic Flask project using `.venv` and `pip`

**Summary:** This creates a Flask project with a `.venv` virtual environment and `requirements.txt`, which can be cloned and set up by running `pip install -r requirements.txt` in the project directory.


## 1. Initialize the Project
Create a new directory for your project and initialize a virtual environment:
```bash
mkdir my-flask-app && cd my-flask-app
python -m venv .venv
```
This command creates a `.venv` directory, which will contain the isolated Python environment for your project.

---

## 2. Activate the Virtual Environment
Activate the virtual environment to install dependencies:

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```bash
.venv\Scripts\activate
```

Once activated, your terminal prompt should show the virtual environment name.

---

## 3. Install Flask
Install the required dependencies using `pip`:
```bash
pip install flask
```
This installs Flask and its dependencies.

---

## 4. Create a Basic Flask Application
Create a file `app/main.py` with a simple Flask app:
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```
This is the minimal Flask application that can be run and tested.

---

## 5. Generate `requirements.txt`
To ensure reproducibility, generate a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```
This file lists all installed dependencies and their versions.

---

## 6. Run the Application
You can now run your Flask app in development mode using:
```bash
flask --app app/main.py run --debug
```
This starts the server with auto-reload enabled, and your app will be available at `http://localhost:5000`.

For production, use a production-ready server like Gunicorn:
```bash
pip install gunicorn
```
Then run:
```bash
gunicorn --bind 0.0.0.0:8000 app.main:app
```
This starts the server in production mode, and your app will be available at `http://0.0.0.0:8000`.

---

## 7. Project Structure
Your project should now look like this:
```
my-flask-app/
├── app/
│   └── main.py
├── .venv/
├── requirements.txt
└── README.md
```
This structure is now ready to be cloned and set up by anyone using:
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---
