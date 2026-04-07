document.addEventListener('DOMContentLoaded', () => {
    const todoInput = document.getElementById('todo-input');
    const addTodoBtn = document.getElementById('add-todo-btn');
    const todoList = document.getElementById('todo-list');

    // Base URL for the backend API
    const API_BASE_URL = 'http://localhost:3000/api/todos';

    // Fetch todos from the backend
    const fetchTodos = async () => {
        try {
            const response = await fetch(API_BASE_URL);
            if (!response.ok) {
                throw new Error('Failed to fetch todos');
            }
            const todos = await response.json();
            renderTodos(todos);
        } catch (error) {
            console.error('Error fetching todos:', error);
        }
    };

    // Render todos to the DOM
    const renderTodos = (todos) => {
        todoList.innerHTML = '';
        todos.forEach(todo => {
            const li = document.createElement('li');
            li.className = todo.completed ? 'completed' : '';
            li.innerHTML = `
                <span>${todo.title}</span>
                <div>
                    <button class="complete-btn" data-id="${todo.id}">
                        ${todo.completed ? 'Undo' : 'Complete'}
                    </button>
                    <button class="delete-btn" data-id="${todo.id}">Delete</button>
                </div>
            `;
            todoList.appendChild(li);
        });
    };

    // Add a new todo
    const addTodo = async () => {
        const title = todoInput.value.trim();
        if (!title) return;

        try {
            const response = await fetch(API_BASE_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, completed: false }),
            });

            if (!response.ok) {
                throw new Error('Failed to add todo');
            }

            todoInput.value = '';
            fetchTodos();
        } catch (error) {
            console.error('Error adding todo:', error);
        }
    };

    // Toggle todo completion status
    const toggleTodo = async (id) => {
        try {
            const response = await fetch(`${API_BASE_URL}/${id}`);
            if (!response.ok) {
                throw new Error('Failed to fetch todo');
            }
            const todo = await response.json();

            const updatedResponse = await fetch(`${API_BASE_URL}/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ...todo, completed: !todo.completed }),
            });

            if (!updatedResponse.ok) {
                throw new Error('Failed to update todo');
            }

            fetchTodos();
        } catch (error) {
            console.error('Error toggling todo:', error);
        }
    };

    // Delete a todo
    const deleteTodo = async (id) => {
        try {
            const response = await fetch(`${API_BASE_URL}/${id}`, {
                method: 'DELETE',
            });

            if (!response.ok) {
                throw new Error('Failed to delete todo');
            }

            fetchTodos();
        } catch (error) {
            console.error('Error deleting todo:', error);
        }
    };

    // Event listeners
    addTodoBtn.addEventListener('click', addTodo);

    todoInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            addTodo();
        }
    });

    todoList.addEventListener('click', (e) => {
        if (e.target.classList.contains('delete-btn')) {
            const id = e.target.getAttribute('data-id');
            deleteTodo(id);
        } else if (e.target.classList.contains('complete-btn')) {
            const id = e.target.getAttribute('data-id');
            toggleTodo(id);
        }
    });

    // Initial fetch
    fetchTodos();
});