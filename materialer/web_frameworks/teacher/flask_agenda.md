# Flask App Creation Workflow Sheet

## **1. Setup**
- **Install Flask**: Run `pip install flask` in your terminal.
- **Create a project folder**: Organize your files (e.g., `app.py`, `templates/`, `static/`).

#### **2. Create a Minimal Flask App**
- **Import Flask**: `from flask import Flask`
- **Initialize the app**: `app = Flask(__name__)`
- **Define a route**: Use `@app.route('/')` to map a URL to a function.
- **Run the app**: Use `flask --app app.py run` in the terminal.

**Example:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

#### **3. Routes**
- **Basic routes**: Use `@app.route('/url')` to define different pages.
- **Dynamic routes**: Use `<variable>` in the route to capture values (e.g., `/user/<username>`).
- **HTTP methods**: Specify allowed methods with `methods=['GET', 'POST']`.

**Example:**
```python
@app.route('/user/<username>')
def show_user(username):
    return f"User: {username}"
```

---

#### **4. Parameters**
- **URL parameters**: Access with `request.args.get('param')`.
- **Form data**: Access with `request.form['field']`.

**Example:**
```python
from flask import request

@app.route('/search')
def search():
    query = request.args.get('q')
    return f"Searching for: {query}"
```

---

#### **5. Requests**
- **Access request data**: Use `request.method`, `request.args`, `request.form`.
- **File uploads**: Use `request.files['file']` and `file.save(path)`.

**Example:**
```python
from flask import request

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"uploads/{file.filename}")
    return "File uploaded!"
```

---

#### **6. Templates**
- **Render templates**: Use `render_template('file.html', var=value)`.
- **Template folder**: Store HTML files in `templates/`.

**Example:**
```python
from flask import render_template

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)
```

---

#### **7. Flash Messages**
- **Flash messages**: Use `flash('message')` and `get_flashed_messages()` in templates.

**Example:**
```python
from flask import flash, redirect, url_for

@app.route('/login', methods=['POST'])
def login():
    flash('Login successful!', 'success')
    return redirect(url_for('home'))
```

---

#### **8. Debug Mode**
- **Enable debug mode**: Run with `flask --app app.py run --debug`.
- **Auto-reload**: Code changes trigger server restart.
- **Error pages**: Detailed error messages in the browser.

---

#### **8.5. CORS (Cross-Origin Resource Sharing)**
**What is CORS?**
CORS is a security feature implemented by web browsers to restrict web pages from making requests to a different domain than the one that served the web page. If your Flask app serves an API that needs to be accessed from a web page hosted on a different domain, you must enable CORS.

**How to Enable CORS in Flask:**
1. **Install the extension:**
   ```bash
   pip install flask-cors
   ```
2. **Enable CORS for your app:**
   ```python
   from flask import Flask
   from flask_cors import CORS

   app = Flask(__name__)
   CORS(app)  # This will enable CORS for all routes
   ```
3. **Enable CORS for specific routes:**
   ```python
   from flask_cors import cross_origin

   @app.route("/api/data")
   @cross_origin()  # This will enable CORS only for this route
   def get_data():
       return {"data": "example"}
   ```
4. **Customize CORS options (optional):**
   ```python
   CORS(app, resources={r"/api/*": {"origins": "*"}})
   ```
   - Replace `*` with specific domains if you want to restrict access.

**Why is CORS important?**
- It allows your frontend (e.g., a React or Vue.js app) to safely interact with your Flask backend, even if they are hosted on different domains.
- Without CORS, browsers will block requests from your frontend to your backend, resulting in errors.

---

#### **9. File Upload**
- **Handle uploads**: Use `request.files` and `secure_filename`.
- **Save files**: Use `file.save(path)`.

**Example:**
```python
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(f"uploads/{filename}")
    return "File saved!"
```

---

### **Summary Table**


Flask Workflow Summary


| Step         | Action                                      | Example Code/Command                     |
|--------------|---------------------------------------------|------------------------------------------|
| Setup        | Install Flask, create folder structure       | `pip install flask`                      |
| Minimal App  | Create app, define route, run server         | `flask --app app.py run`                 |
| Routes       | Define URL routes, dynamic routes           | `@app.route('/user/<username>')`         |
| Parameters   | Access URL/form parameters                  | `request.args.get('q')`                  |
| Requests     | Handle GET/POST, file uploads               | `request.files['file']`                  |
| Templates    | Render HTML templates                       | `render_template('file.html')`           |
| Flash        | Show user feedback messages                 | `flash('Message')`                        |
| Debug        | Enable debug mode                           | `flask --app app.py run --debug`         |
| CORS         | Enable cross-origin requests                | `CORS(app)`                               |
| File Upload  | Securely save uploaded files                | `file.save(f"uploads/{filename}")`       |

---

