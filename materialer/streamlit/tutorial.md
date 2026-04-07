# Streamlit Tutorial

**Documentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)

---

## **1. Installation and Setup**

### **Install Streamlit**

To get started, install Streamlit using pip:

```bash
pip install streamlit
```

### **Create a `requirements.txt` File**

It's good practice to list all dependencies in a `requirements.txt` file. For a basic Streamlit app, your file might look like this:

```
streamlit==1.29.0
pandas==2.0.3
numpy==1.24.3
```

Install dependencies from the file:

```bash
pip install -r requirements.txt
```

---

## **2. Basic Text Elements**

### **Hello World**

Create a file named `app.py` and add the following code:

```python
import streamlit as st

st.title("Hello World!")
st.write("Welcome to my first Streamlit app.")
```

### **Markdown Support**

Streamlit supports Markdown syntax for rich text formatting:

```python
st.markdown("""
# Hello world
Here are some paragraph text.

## We are using markdown
* Point 1
* Point 2
* Point 3
""")
```

or just:

```python
"""
# Hello world
Here are some paragraph text.

## We are using markdown
* Point 1
* Point 2
* Point 3
"""
```







### Run the app:

```bash
streamlit run app.py
```

### **Dynamic Text with Variables**

```python
name = "Claus"
st.write(f"Hello, {name}!")
```

---

## **3. Interactive Widgets**

### **Slider**

```python
x = st.slider("Antal biler", 0, 100, 10)
st.write(f"Du har valgt {x} biler.")
```

### **Text Input**

```python
y = st.text_input("Hvad er din alder?")
st.write(f"Din alder er: {y}")
```

### **Button**

```python
if st.button("Click me"):
    st.write("Button clicked!")
```

### **Selectbox**

```python
s = st.selectbox("Hvad er din alder?", [12, 13, 33, 66])
if s >= 18:
    st.write(f"Hello, {s}!")
else:
    st.write("Du er ikke gammel nok.")
```

---

## **4. Layout: Columns and Sidebar**

### **Columns**

```python
col1, col2 = st.columns(2)
with col1:
    st.button("Click me")
with col2:
    st.write("# Hello there")
```

### **Sidebar**

```python
st.sidebar.title("Sidebar")
st.sidebar.button("Click me")
```

---

## **5. Organizing Your App with Pages**

### **Create a `pages` Folder**

Streamlit supports multi-page apps. Create a folder named `pages` in the same directory as your main app. Each file in the `pages` folder will appear as a separate page in your app.

Example:

```
my_app/
├── app.py
└── pages/
    ├── page1.py
    └── page2.py
```
---

## **6. Example: Complete App**

```python
import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Hvad er dit navn?")
age = st.slider("Hvad er din alder?", 0, 100, 25)

if st.button("Submit"):
    if age >= 18:
        st.success(f"Velkommen, {name}!")
    else:
        st.error("Du er ikke gammel nok.")

st.sidebar.title("Navigation")
st.sidebar.button("Home")
st.sidebar.button("About")
```

