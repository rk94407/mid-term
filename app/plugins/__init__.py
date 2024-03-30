class Command:
    def run(self):
        raise NotImplementedError("Command must implement a run method")

    @staticmethod
    def command_name():
        raise NotImplementedError("Command must have a command_name class method")

class StartApp(Command):
    @staticmethod
    def command_name():
        return "start"

    def run(self):
        print("Starting the application...")

class ShowHelp(Command):
    @staticmethod
    def command_name():
        return "help"

    def run(self):
        print("Showing help information...")

class QuitApp(Command):
    @staticmethod
    def command_name():
        return "quit"

    def run(self):
        print("Quitting the application...")
        exit(0)

class SayHello(Command):
    @staticmethod
    def command_name():
        return "hello"

    def run(self):
        print("Hello!")

class SayBye(Command):
    @staticmethod
    def command_name():
        return "bye"

    def run(self):
        print("Goodbye!")

def load_commands():
    commands = {}
    # Assuming all command classes are defined in this file for simplicity
    # In a real plugin system, you might dynamically import modules or use a plugin discovery mechanism
    for command_class in Command.__subclasses__():
        command_instance = command_class()
        commands[command_class.command_name()] = command_instance.run
    return commands

def display_menu(commands):
    print("Available commands:")
    for command in commands.keys():
        print(f"- {command}")

def main():
    commands = load_commands()
    display_menu(commands)
    while True:
        user_input = input("Enter command: ").strip().lower()
        if user_input in commands:
            commands[user_input]()
        else:
            print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    main()
