def validator(*args):
    """
    Checks if user input is an integer.
    Parameters:
        *args (String) : "+" Checks for positive integers;
                         "-" Checks for negative integers;
                         "" Checks for any integers;
    """
    while True:
        try:
            user_input = int(input())
        except ValueError:
            print("Please input a number!")
        else:
            if user_input < 0 and args[0] == '+':
                print("Please input a positive number!")
                pass
            elif user_input > 0 and args[0] == '-':
                print("Please input a negative number!")
                pass
            else:
                break
    return user_input
