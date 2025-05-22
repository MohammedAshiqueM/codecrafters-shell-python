import sys


def main():
    # Uncomment this block to pass the first stage
    
    while(True):
        sys.stdout.write("$ ")

        # built in commands
        shell_builtin = {'echo','exit','type'}
        #user input
        command = input()
        command_list = command.split()
        #checking the shell commads
        if command == 'exit 0':
            break
        elif command_list[0] == 'echo':
            print(command[5:])
            continue
        elif command_list[0] == 'type':
            if command_list[1] in shell_builtin:
                print(f'{command_list[1]} is a shell builtin')
            else:
                print(f'{command_list[1]}: not found')
            continue
        else:
            print(f'{command}: command not found')

if __name__ == "__main__":
    main()
