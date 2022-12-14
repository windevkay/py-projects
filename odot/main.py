import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    # match params and cases can be used as well
    if user_action.startswith('add'):
        # extract everything else that comes after 'add' (slicing)
        todo = user_action[4:] + "\n"
        # read existing todos
        todos = functions.get_todos()

        todos.append(todo)
        # save item on disk
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        # remove trailing newline chars - list comp
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1}- {item}")

    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:]) - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ") + '\n'
            # replace existing item with the new one
            todos[index] = new_todo
            functions.write_todos(todos)
        except ValueError:
            print('Invalid Command')
            continue

    elif user_action.startswith('complete'):
        try:
            index = int(user_action[9:]) - 1
            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            # removes the item from the list
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo: {todo_to_remove} - was removed from the list"
            print(message)
        except IndexError:
            print('No item with that index')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Invalid Command')

print("...exiting!")
