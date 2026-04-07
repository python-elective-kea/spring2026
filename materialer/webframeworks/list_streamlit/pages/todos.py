import streamlit as st
import requests

# FastAPI server URL (adjust if needed)
FASTAPI_URL = "http://localhost:3000"

st.title("Todo App with FastAPI + Streamlit")

# Initialize session state for todos
if "todos" not in st.session_state:
    st.session_state.todos = []

# Fetch all todos
def fetch_todos():
    response = requests.get(f"{FASTAPI_URL}/api/todos")
    if response.status_code == 200:
        st.session_state.todos = response.json()
    else:
        st.error("Failed to fetch todos")

# Create a new todo
def create_todo(title, completed):
    response = requests.post(
        f"{FASTAPI_URL}/api/todos",
        json={"title": title, "completed": completed}
    )
    if response.status_code == 200:
        fetch_todos()  # Refresh the list
        return True
    else:
        st.error("Failed to create todo")
        return False

# Update a todo
def update_todo(todo_id, title=None, completed=None):
    data = {}
    if title is not None:
        data["title"] = title
    if completed is not None:
        data["completed"] = completed
    response = requests.put(
        f"{FASTAPI_URL}/api/todos/{todo_id}",
        json=data
    )
    if response.status_code == 200:
        fetch_todos()  # Refresh the list
    else:
        st.error("Failed to update todo")

# Delete a todo
def delete_todo(todo_id):
    response = requests.delete(f"{FASTAPI_URL}/api/todos/{todo_id}")
    if response.status_code == 200:
        fetch_todos()  # Refresh the list
        return True
    else:
        st.error("Failed to delete todo")
        return False

# UI for listing and managing todos
st.header("Your Todos")
fetch_todos()  # Initial fetch

if st.session_state.todos:
    for todo in st.session_state.todos:
        st.subheader(f"{todo['title']}")
        st.write(f"Status: {'Completed' if todo['completed'] else 'Pending'}")

        # Toggle completion status
        new_status = st.checkbox("Mark as completed", value=todo["completed"], key=f"status_{todo['id']}")
        if new_status != todo["completed"]:
            update_todo(todo["id"], completed=new_status)

        # Delete button
        if st.button(f"Delete Todo {todo['id']}"):
            delete_todo(todo["id"])

else:
    st.info("No todos found. Add one above!")

# UI for creating a new todo
st.header("Create a New Todo")
new_title = st.text_input("Title")
new_completed = st.checkbox("Completed")
if st.button("Add Todo"):
    if new_title:
        if create_todo(new_title, new_completed):
            st.success(f"Todo added: {new_title}")
            st.rerun()
    else:
        st.warning("Please enter a title")
