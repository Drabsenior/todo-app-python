import functions
import PySimpleGUI as sg

label = sg.Text('Type in a todo: ')
input_box = sg.Input(tooltip='Enter todo', key='todo' )
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos() , key='todos', size=[45, 10], enable_events=True)
edit_button = sg.Button('Edit')
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button], [list_box,edit_button]], font=('Helvetica' ,16))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            print(todos)
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            print('hello')
            print(values['todo'])
            print(values['todos'][0])
            window['todo'].update(value=values['todos'][0])
        case 'Edit':
            todos = functions.get_todos()
            edit_input = values['todos'][0]
            index = todos.index(edit_input)
            todos[index] = values['todo'] + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break

window.close()
