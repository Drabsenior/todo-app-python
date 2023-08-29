import streamlit as st
import functions

todos = functions.get_todos()

st.title('Todo App')
st.subheader('simple todo app')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder='Add todos...')

