import functions
import PySimpleGUI as sg
import time

sg.theme('black')
clock = sg.Text('', key='clock')
label = sg.Text('Type in a todo: ')
input_box = sg.Input(tooltip='Enter todo', key='todo')
add_button = sg.Button('Add',  image_size=[60,30], tooltip='Add todo', key='Add')
list_box = sg.Listbox(values=functions.get_todos() , key='todos', size=[45, 10], enable_events=True)
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
window = sg.Window('My To-Do App', layout=[[clock],
                                           [label],
                                           [input_box, add_button],
                                           [list_box,edit_button, complete_button],
                                           [exit_button]
                                           ], font=('Helvetica', 16))


while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Edit':
            try:
                new_todo = values['todo'].replace('\n', "")
                print(new_todo + 'first')
                todos = functions.get_todos()
                edit_input = values['todos'][0]
                index = todos.index(edit_input)
                todos[index] = new_todo + '\n'
                print(new_todo, 'real')
                functions.write_todos(todos)
                print(todos , 'final')
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select item to edit !", font=('Helvetica', 16))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select item to complete !", font=('Helvetica', 16))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
