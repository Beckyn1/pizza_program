
def get_string(m):
    user_input = input(m)
    return user_input

def menu_pizza(p):
    for i in range(len(p)):
        print("{}: ${}".format(p[i][0], p[i][1]))

def main():

    pizza_list = [
        ["Cheese", 5],
        ["Pepperoni", 5],
        ["Hawaiian", 5],
        ["Meatlovers", 5]
    ]

    run_program = True
    while run_program:
        print("-" * 42)
        order_choice = get_string("Please select an option =>")
        if order_choice == "M":
            menu_pizza(pizza_list)
            run_program = False
        elif order_choice == "Q":
            print("Thank you for choosing Papa's Pizzeria!")
            run_program = False
        else:
            print("Unrecognised entry must be A or R")


if __name__ == "__main__":
    main()