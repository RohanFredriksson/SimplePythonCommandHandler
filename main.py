import sys
import os

path = 'commands'

def main():

    # Find all files in the command folder, and all available commands.
    files = os.listdir(os.path.join(path))
    command_files = [command_file for command_file in files if '.py' in command_file]
    commands = [command[:-3] for command in command_files]
    commands_lower = [command.lower() for command in commands]

    # If no arguments have been given, display help.
    if len(sys.argv) == 1:
        print('\nPlease select one of the following commands:')
        for command in commands:
            print(" - " + command)
        print('\nFor example, python3 main.py <command>\n')
        exit()

    # Determine whether the argument provided is a valid command.
    arg = sys.argv[1]
    arg = arg.lower()

    # If argument contains .py on the end, strip it off.
    if len(arg) > 3:
        if arg[-3:] == '.py':
            arg = arg[:-3]

    # Check whether the argument is in the known command list.
    if arg not in commands_lower:
        print('\nInvalid command.')
        print('\nPlease select one of the following commands:')
        for command in commands:
            print(" - " + command)
        print('\nFor example, python3 main.py <command>\n')
        exit()

    # Find the command and run it.
    for command in commands:
        if arg.lower() == command.lower():
            # Spawn a new shell process to run program.
            os.system('python3 ./' + path + '/' + command + '.py')
    
if __name__ == '__main__':
	main()