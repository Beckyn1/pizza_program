import re


def get_num(m):
    my_integer = input(m)
    length = len(my_integer)
    if re.match(r"^(64|04|027|021|022|020)", my_integer):
        if length < 9:
            print("Invalid Phone Number")
            return get_phone()
        elif length > 12:
            print("Invalid Phone Number")
            return get_phone()
        elif not re.match('^[0-9()$%_/.]*$', my_integer):
            print("Invalid Phone Number")
            return get_phone()
        else:
            return my_integer
    else:
        print("Invalid Phone Number")
        return get_phone()


def get_phone():
    phone = get_num("What is your phone number?")
    print(phone)
    return phone


get_phone()

