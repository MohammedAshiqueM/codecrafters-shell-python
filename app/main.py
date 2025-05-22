from genericpath import isfile
import sys
import os
import subprocess

def main():
    # Uncomment this block to pass the first stage
        
    def IsExecutable(command):
        """To check executable file in PATH"""
        paths = os.environ.get('PATH','').split(os.pathsep)
    
        for dir in paths:
            ex = os.path.join(dir, command)
            if os.path.isfile(ex) and os.access(ex, os.X_OK):
                return ex
        return None
    
    def Execute(command_list):
        """To execute the command"""
        path = IsExecutable(command_list[0])
        if path:
            result = subprocess.run([command_list[0]] + command_list[1:], capture_output=True, text=True)     
            return(result.stdout)
        return None
            
    while(True):
        sys.stdout.write("$ ")

        # built in commands
        shell_builtin = {'echo','exit','type'}
        #user input
        command = input()
        command_list = command.split()
        #checking the shell commads
        if command == 'exit 0':
            # exit the terminal
            break
        elif command_list[0] == 'echo':
            # print the statement
            print(command[5:])
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
        else:
            result = Execute(command_list)
            if result:
                print(result)
            else:
                print(f'{command_list[0]}: command not found')
                
if __name__ == "__main__":
    main()
