# Todo App Frontend

This is a simple todo app frontend that communicates with a REST API backend. The backend is not provided and should be implemented as an exercise.

## Required Backend Routes

The frontend expects the following REST API endpoints:

### GET `/api/todos`
- **Description**: Fetch all todos
- **Response**: Array of todo objects
- **Example Response**:
  ```json
  [
    {
      "id": 1,
      "title": "Buy groceries",
      "completed": false
    },
    {
      "id": 2,
      "title": "Do laundry",
      "completed": true
    }
  ]
  ```

### POST `/api/todos`
- **Description**: Add a new todo
- **Request Body**:
  ```json
  {
    "title": "New todo",
    "completed": false
  }
  ```
- **Response**: The created todo object

### GET `/api/todos/:id`
- **Description**: Fetch a specific todo by ID
- **Response**: The todo object

### PUT `/api/todos/:id`
- **Description**: Update a todo
- **Request Body**:
  ```json
  {
    "title": "Updated todo",
    "completed": true
  }
  ```
- **Response**: The updated todo object

### DELETE `/api/todos/:id`
- **Description**: Delete a todo
- **Response**: Empty response or confirmation message

## Setup

1. Clone this repository.
2. Open `index.html` in a web browser.
3. Ensure the backend is running and accessible at `http://localhost:3000`.

## Features

- Add new todos
- Mark todos as complete/incomplete
- Delete todos
- Fetch and display todos from the backend

## Notes

- The frontend assumes the backend is running on `http://localhost:3000`. Adjust the `API_BASE_URL` in `script.js` if your backend uses a different URL.
- Error handling is minimal and logs errors to the console. Enhance as needed for production use.


