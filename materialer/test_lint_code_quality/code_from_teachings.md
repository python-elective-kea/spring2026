## Code demo from teachings

### 1. **uv** (Project Setup)
```bash
uv init --lib mymath
cd mymath
uv add numpy
```

### 2. **ruff** (Linting)
```bash
uv add --dev ruff
uv run ruff check --fix .
```

### 3. **pytest** (Testing)
```python
# mymath/mymath.py
def add(a: int, b: int) -> int:
    return a + b
```
```python
# tests/test_mymath.py
from mymath.mymath import add

def test_add():
    assert add(2, 3) == 5
```
```bash
uv add --dev pytest
uv run pytest
```

### 4. **pyright** (Type Checking)
```bash
uv add --dev pyright
uv run pyright
```

### 5. **PEP 8** (Style Guide)
```python
# Follow PEP 8 in your code!
def add(a: int, b: int) -> int:
    return a + b
```

---

### 6. **Git Hooks** (Automate Checks)
**Purpose:** Run linters and tests before commits/pushes.

#### Setup:
```bash
# Install pre-commit
uv add --dev pre-commit
```
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.4
    hooks:
      - id: ruff
        args: [--fix]
  - repo: local
    hooks:
      - id: pytest
        name: Run tests
        entry: uv run pytest
        language: system
        pass_filenames: false
```
```bash
# Install hooks
uv run pre-commit install
```
**Demo:**

- Try to commit code with a PEP 8 violation or failing test. The hook will block the commit until fixed.
- Remeber to create a .gitignore file and add:

```
__pycache__/
*.pyc
*.pyo
.pytest_cache/
```

---

## Live Coding Script

**1. Intro (2 min):**
“Today, we’ll set up a Python project with modern tools: `uv` for project management, `ruff` for linting, `pytest` for testing, `pyright` for type checking, and git hooks to automate quality checks.”

**2. Project Setup:**
```bash
uv init --lib mymath
cd mymath
uv add numpy
```

**3. Add Code:**
```python
# mymath/mymath.py
def add(a: int, b: int) -> int:
    return a + b
```

**4. Linting:**
```bash
uv add --dev ruff
uv run ruff check --fix .
```

**5. Testing:**
```python
# tests/test_mymath.py
from mymath.mymath import add

def test_add():
    assert add(2, 3) == 5
```
```bash
uv add --dev pytest
uv run pytest
```

**6. Type Checking:**
```bash
uv add --dev pyright
uv run pyright
```

**7. Git Hooks:**
```bash
uv add --dev pre-commit
# Create .pre-commit-config.yaml (as above)
uv run pre-commit install
# Demo: Try to commit bad code
```

**8. Wrap-up:**
“Now you have a project with automated linting, testing, and type checking!”

---
