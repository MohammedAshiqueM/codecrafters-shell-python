import os
import subprocess

def print_echo(command_list):
    for i in command_list:
        print(i,end=' ')
    print()
        
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

def read_file(command_list):
    try:
        res = ''
        for i in command_list:
            with open(i, 'r') as f:
                res+=f.read()
        return res
    except:
        print(f'cannot find path {i}')
        