def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def print_list(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None


def order_pizza(l):
    for i in range(0, len(l)):
        output = "{}: {} {}".format(i, l[i][1], l[i][0])
        print(output)
    order_choice = get_integer("What pizza number do you want?")
    if -1 < order_choice < len(l):
        print("{} is chosen".format(l[order_choice][0]))
    else:
        print("Unrecognisable entry")


def main():

    pizza_list = [
        ["Cheese", 2],
        ["Pepperoni", 4]
    ]

    print()
    print("Welcome to Papa's Pizzeria!")
    print("-"*42)
    print("Please select an option from the menu:")
    menu_list = [
        ["P", "Print Menu"],
        ["O", "Order"],
        ["Q", "Quit"]
    ]
    run_program = True
    while run_program:
        for x in menu_list:

            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("-" * 42)
        user_choice = get_string("Please select an option: -> ")
        print("-" * 42)
        if user_choice == "P":
            print_list(pizza_list)
        elif user_choice == "O":
            order_pizza(pizza_list)
        elif user_choice == "Q":
            print("Thank you for ordering with Papa's Pizzeria!")
            run_program = False
        else:
            print("Unrecognised entry must be P, O or Q")


if __name__ == "__main__":

    main()
