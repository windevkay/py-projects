while True:
    user_action = input("Type add, show (or display), edit, complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            # read existing todos
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            # save todo on disk
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # remove trailing newline chars - list comp
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1}- {item}")

        case 'edit':
            index = int(input("Index of todo to edit: ")) - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ") + '\n'
            # replace existing todo with the new one
            todos[index] = new_todo
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            index = int(input("Index of todo to complete: ")) - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[index].strip('\n')
            # removes the todo from the list
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo: {todo_to_remove} - was removed from the list"
            print(message)

        case 'exit':
            break
        case _:
            print("Unknown or Invalid command")

print("...exiting!")
