# from functions import get_todos, write_todos

import functions     #(have to include 'funtions.' before use of function)
import time

print(time.strftime("%b %d, %Y %H:%M:%S"))
while 2 > 1:
    userAction = input("Type add, show, edit, complete or exit: ")
    userAction = userAction.strip()

    if userAction.startswith('add'):
        todo = userAction[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif userAction.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item}")
    elif userAction.startswith('edit'):
        try:
            number = int(userAction[5:])
            number -= 1

            todos = functions.get_todos()

            newTodo = input('Enter new todo: ')
            todos[number] = newTodo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print('Your command is not valid')
            continue

    elif userAction.startswith('complete'):
        try:
            number = int(userAction[9:])

            todos = functions.get_todos()

            popped = todos.pop(number - 1)
            popped = popped.strip('\n')

            functions.write_todos(todos)

            message = f'Todo {popped} was removed from the list'
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue

    elif userAction.startswith('exit'):
        break
    else:
        print("command is invalid")


print("Bye!")
