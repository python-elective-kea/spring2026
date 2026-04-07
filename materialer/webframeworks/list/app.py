from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Tilføj CORS for at tillade anmodninger fra frontend

app = Flask(__name__)
CORS(app)  # Aktiver CORS for alle ruter

# Servér index.html
@app.route("/") # python app.py 
def serve_index():
    return render_template("index.html")


# Simpel "database" (liste af todos)
todos = [
    {"id": 1, "title": "Todo 1", "completed": False}
]

# Hjælpefunktion til at finde et todo efter ID
def find_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None

# Læs alle todos (Read)
@app.route("/api/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

# Læs et enkelt todo (Read)
@app.route("/api/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)

# Opret et nyt todo (Create)
@app.route("/api/todos", methods=["POST"])
def create_todo():
    if not request.json or "title" not in request.json:
        return jsonify({"error": "Title is required"}), 400

    new_todo = {
        "id": len(todos) + 1,
        "title": request.json["title"],
        "completed": request.json.get("completed", False)
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Opdater et todo (Update)
@app.route("/api/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo)

# Slet et todo (Delete)
@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todo = find_todo(todo_id)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"result": "Todo deleted"})

if __name__ == "__main__":
    app.run(debug=True, port=3000)  # Kør på port 3000 for at matche frontend
