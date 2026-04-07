# Streamlit Requests Tutorial

This tutorial will guide you through creating a Streamlit application that reads data from an external API.

## Step 1: Install Required Packages

First, install the necessary packages:

```bash
pip install streamlit requests
```

## Step 2: Create a Streamlit App

Create a new file named `app.py` and add the following code:

```python
import streamlit as st
import requests

# Set the title of the app
st.title("Streamlit Requests Tutorial")

# Add a button to fetch data
if st.button("Fetch Data"):
    # Replace with the API endpoint you want to fetch data from
    api_url = "http://20.100.199.144/api/todos"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        # Display the fetched data in a nice format
        st.success("Data fetched successfully!")
        
        # Display each todo item in a nice format
        for item in data:
            st.markdown(f"""
            ### Todo Item
            - **ID**: {item['id']}
            - **Title**: {item['title']}
            - **Completed**: {'Yes' if item['completed'] else 'No'}
            """)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
```

## Step 3: Run the Streamlit App

Start the Streamlit application:

```bash
streamlit run app.py
```

## Step 4: Test the App

Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`). Click the "Fetch Data" button to fetch data from the external API.

## Notes
- Ensure the external API (`http://20.100.199.144/api/todos`) is accessible from your environment.
- Handle errors appropriately in a production environment.
- Consider adding authentication if the external API requires it.

## Troubleshooting

If you encounter the error `Error fetching data: Expecting value: line 2 column 5 (char 5)`, it may be due to:

1. **Network Issues**: Ensure your environment can access the external API.
2. **CORS Issues**: If running in a browser, CORS policies might block the request.
3. **Streamlit Environment**: Try running the API request outside Streamlit to isolate the issue.

To test the API directly, create a Python script:

```python
import requests

api_url = "http://20.100.199.144/api/todos"

try:
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    print("Success:", data)
except requests.exceptions.RequestException as e:
    print("Error:", e)
```

Run it with:

```bash
python test_api.py
```

If this works, the issue is likely with the Streamlit environment or network configuration.
