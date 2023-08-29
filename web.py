import streamlit as st
import functions


def add_todo():
    todo = st.session_state['todo_input'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title('Todo App')
st.subheader('simple todo app')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='todo', placeholder='Add todos...', on_change=add_todo, key='todo_input' , label_visibility='hidden')

st.session_state
