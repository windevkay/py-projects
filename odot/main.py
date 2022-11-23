user_prompt = "Type add, show (or display), edit or exit: "
todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            index = int(input("Index of todo to edit: "))
            new_todo = input("Enter new todo: ")
            # replace existing todo with the new one
            todos[index - 1] = new_todo
        case 'exit':
            break
        case _:
            print("Unknown or Invalid command")

print("...exiting!")
