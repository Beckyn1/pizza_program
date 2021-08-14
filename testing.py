import re

def get_integer(m):
    my_integer = int(input(m))
    return str(my_integer)

def val_phone(str):
    """Phone number validation function."""
    str = re.sub(r"\D", "", str)
    valid = True
    # this tests to match the starting numbers with the rest of the number
    if re.match(r"^(64|04|02)", str):
        # if the number starts with 64 the total amount of letter have to be 10-13
        if re.match(r"^64", str) and (len(str) < 10 or len(str) > 13):
            valid = False
        # if the number starts with 04 the total amount of letter have to be 8 or 9
        elif re.match(r"^04", str) and (len(str) < 8 or len(str) > 9):
            valid = False
        # if the number starts with 021, 022, 027 the total amount of letter have to be 10 or 11
        elif re.match(r"^(021|022|027)", str) and (len(str) < 10 or len(str) > 11):
            valid = False
    else:
        valid = False
    if valid:
        return str
    # if number doesn't appear valid, the user is asked to re-enter
    else:
        print("This doesn't appear to be a valid phone number")
        return get_phone()

def get_phone():
    phone = get_integer("what is your phone number")
    val_phone(phone)

get_phone()

# len with integers version of testing