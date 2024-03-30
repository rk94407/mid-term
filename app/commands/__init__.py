# 

commands = {
    "start": start_app,
    "help": show_help,
    "quit": quit_app,
    "hello": hello,
    "bye": bye,
    
}

def display_menu():
    print("Available commands:")
    for command in commands.keys():
        print(f"- {command}")


commands["menu"] = display_menu


def main():
    display_menu()  
    while True:
        user_input = input("Enter command: ")
        if user_input in commands:
            commands[user_input]()  
        else:
            print("Unknown command. Type 'menu' to see available commands.")