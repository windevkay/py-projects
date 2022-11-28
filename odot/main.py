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
            for index, item in enumerate(todos):
                item = item.title()
                print(f"{index + 1}- {item}")
        case 'edit':
            index = int(input("Index of todo to edit: "))
            new_todo = input("Enter new todo: ")
            # replace existing todo with the new one
            todos[index - 1] = new_todo
        case 'complete':
            index = int(input("Index of todo to complete: "))
            # removes the todo from the list
            todos.pop(index - 1)
        case 'exit':
            break
        case _:
            print("Unknown or Invalid command")

print("...exiting!")
