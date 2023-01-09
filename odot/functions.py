def get_todos(filepath='todos.txt'):
    """ Read a text file and return its content (todos) """
    with open(filepath, 'r') as fileReader:
        result = fileReader.readlines()
    return result


def write_todos(args, filepath='todos.txt'):
    """ Accept a new set of todos and write to a text file """
    with open(filepath, 'w') as fileWriter:
        fileWriter.writelines(args)
