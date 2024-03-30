def start_app():
    print("Starting the application...")

def show_help():
    print("Showing help information...")

def quit_app():
    print("Quitting the application...")
    exit(0)

def display_menu():
    print("Available commands:")
    for command in commands.keys():
        print(f"- {command}")

def hello():
    print("Hello!")

def bye():
    print("GoodBye!")

commands = {
    "start": start_app,
    "help": show_help,
    "quit": quit_app,
    "menu": display_menu,
    "hello": hello,
    "bye": bye,
    "exit": quit_app,
}

def main():
    display_menu()
    while True:
        user_input = input("Enter command: ").strip().lower()
        if user_input in commands:
            commands[user_input]()
        else:
            print("Unknown command. Type 'menu' to see available commands.")


if __name__ == "__main__":
    main()