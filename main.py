from functions import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print('the time below')
print('It is ', now)
while True:
    input_todos = input('Type add, show, edit,complete or exit: ')

    input_todos = input_todos.strip()

    if input_todos.startswith("add") or input_todos.startswith("new"):
        todos = get_todos()

        todo = input_todos[4:] + "\n"
        todos.append(todo)

        write_todos(todos)
    elif input_todos.startswith("show"):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif input_todos.startswith("edit"):
        try:
            input_number = int(input_todos[5:])
            index = input_number - 1

            todos = get_todos()
            todo_to_edit = todos[index].strip('\n')

            edit_todo = input('Enter the edit todo: ')
            todos[index] = edit_todo + '\n'

            write_todos(todos)

            message = f"Todo {todo_to_edit} has been edited"
            print(message)

        except ValueError:
            print("Your command is not Valid")
            continue
    elif input_todos.startswith("complete"):
        try:
            input_number = int(input_todos[9:])
            index = input_number - 1
            todos = get_todos()
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} has been removed"
            print(message)
        except IndexError:
            print("Item with that number is not found.")
            continue
    elif input_todos.startswith("exit"):
        break
    else:
        print('Command is invalid!')
