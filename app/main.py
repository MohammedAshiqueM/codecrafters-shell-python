from genericpath import isfile
import sys
import shlex
from app.utils import IsExecutable, Execute, read_file, print_echo

def main():
        
    
    while(True):
        sys.stdout.write("$ ")

        # built in commands
        shell_builtin = {'echo','exit','type'}
        #user input
        command = input()
        command_list = shlex.split(command)
        #checking the shell commads
        if command == 'exit 0':
            # exit the terminal
            break
        elif command_list[0] == 'echo':
            # print the statement
            print_echo(command_list)
            continue
        elif command_list[0] == 'type':
            # check the command
            if command_list[1] in shell_builtin:
                print(f'{command_list[1]} is a shell builtin')
            else:
                # check wheather the command is executable path
                path = IsExecutable(command_list[1])
                if path:
                    print(f'{command_list[1]} is {path}')
                else:
                    print(f'{command_list[1]}: not found')
            continue
        elif command_list[0] == 'cat':
            read_file(command_list[1])
        else:
            result = Execute(command_list)
            if result:
                print(result,end='')
            else:
                print(f'{command_list[0]}: command not found')
                
if __name__ == "__main__":
    main()
