import sys


def main():
    # Uncomment this block to pass the first stage
    
    while(True):
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()
        first_word = command.split()[0]
        if command == 'exit 0':
            break
        elif first_word == 'echo':
            print(command[5:])
            continue
        print(f'{command}: command not found')

if __name__ == "__main__":
    main()
