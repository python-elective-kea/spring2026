# Setup basic FastAPI project using `.venv` and `pip`

**Summary:** This creates a FastAPI project with a `.venv` virtual environment and `requirements.txt`, which can be cloned and set up by running `pip install -r requirements.txt` in the project directory.


## 1. Initialize the Project
Create a new directory for your project and initialize a virtual environment:
```bash
mkdir my-fastapi-app && cd my-fastapi-app
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

## 3. Install FastAPI
Install the required dependencies using `pip`:
```bash
pip install fastapi[standard]
```
This installs FastAPI along with all recommended dependencies, including Uvicorn (an ASGI server).

---

## 4. Create a Basic FastAPI Application
Create a file `app/main.py` with a simple FastAPI app:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
This is the minimal FastAPI application that can be run and tested.

---

## 5. Generate `requirements.txt`
To ensure reproducibility, generate a `requirements.txt` file:
```bash
pip freeze > requirements.txt
```
This file lists all installed dependencies and their versions.

---

## 6. Run the Application
You can now run your FastAPI app using:
```bash
fastapi dev app/main.py
```
This starts the server with auto-reload enabled, and your app will be available at `http://localhost:8000`.

For production, use:
```bash
fastapi run app/main.py --host 0.0.0.0 --port 8000
```

---

## 7. Project Structure
Your project should now look like this:
```
my-fastapi-app/
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
