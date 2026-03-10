from flask import Flask, request, jsonify

app = Flask(__name__)

# Simpel "database" (liste af items)
items = [
    {"id": 1, "name": "Item 1", "description": "Description for Item 1"},
    {"id": 2, "name": "Item 2", "description": "Description for Item 2"}
]

# Hjælpefunktion til at finde et item efter ID
def find_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return item
    return None

# Læs alle items (Read)
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# Læs et enkelt item (Read)
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Opret et nyt item (Create)
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or "name" not in request.json:
        return jsonify({"error": "Name is required"}), 400

    new_item = {
        "id": len(items) + 1,
        "name": request.json["name"],
        "description": request.json.get("description", "")
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Opdater et item (Update)
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    return jsonify(item)

# Slet et item (Delete)
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items = [i for i in items if i["id"] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
