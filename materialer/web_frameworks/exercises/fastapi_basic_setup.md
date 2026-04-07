# Setup basic FastAPI project using `uv` and `pyproject.toml`

**Summary:** This creates a FastAPI project with `pyproject.toml` and `uv.lock`, which can be cloned and set up by running `uv sync` in the project directory.


## 1. Initialize the Project
Create a new directory for your project and initialize it with `uv`:
```bash
mkdir my-fastapi-app && cd my-fastapi-app
uv init --app
```
This command creates a basic project structure and a `pyproject.toml` file, which is essential for managing dependencies and project metadata.

---

## 2. Edit `pyproject.toml`
Ensure your `pyproject.toml` includes FastAPI and Uvicorn (or use the `fastapi[standard]` extra for all recommended dependencies). Example:
```toml
[project]
name = "my-fastapi-app"
version = "0.1.0"
description = "FastAPI project"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]",
]
```
This setup ensures all necessary dependencies are included and locked for reproducibility.

---

## 3. Create a Basic FastAPI Application
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

## 4. Sync Dependencies with `uv`
Run the following command to install dependencies and create a virtual environment:
```bash
uv sync
```
This command reads `pyproject.toml`, resolves and locks dependencies (creating a `uv.lock` file), and sets up a virtual environment.

---

## 5. Run the Application
You can now run your FastAPI app using:
```bash
uv run fastapi dev
```
or, for production:
```bash
uv run fastapi run app/main.py --host 0.0.0.0 --port 8000
```
This starts the server, and your app will be available at `http://localhost:8000`.

---

## 6. Project Structure
Your project should now look like this:
```
my-fastapi-app/
├── app/
│   └── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```
This structure is now ready to be cloned and set up by anyone using `uv sync`.

---


