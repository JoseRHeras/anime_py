import sys


def input_loop():
    while(True):

        user_input = input("Please enter your desired: ")
        if user_input == "exit": break        

def main():
    optional_commands = sys.argv

    if len(optional_commands) <= 1: return input_loop()




if __name__ == '__main__':
    main()