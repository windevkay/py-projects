while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    # match params and cases can be used as well
    if 'add' in user_action:
        # extract everything else that comes after 'add' (slicing)
        todo = user_action[4:] + "\n"
        # read existing todos
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)
        # save item on disk
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        # remove trailing newline chars - list comp
        # new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1}- {item}")

    elif 'edit' in user_action:
        index = int(user_action[5:]) - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ") + '\n'
        # replace existing item with the new one
        todos[index] = new_todo
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        index = int(user_action[9:]) - 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[index].strip('\n')
        # removes the item from the list
        todos.pop(index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo: {todo_to_remove} - was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print('Invalid Command')

print("...exiting!")
