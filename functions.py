def get_todos(filepath='todos.txt'):
    """Returns todos in file. Default file is todos.txt"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """
    Open a text file and
    write lines into text
    file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
