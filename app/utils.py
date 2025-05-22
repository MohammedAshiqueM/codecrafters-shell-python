import os
import subprocess


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

def read_file(path):
    try:
        with open(path, 'r') as f:
            print(f.read())
    except:
        print(f'cannot find path {path}')
        