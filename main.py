def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def pick_up(l):
    order(l)


def delivery(l):
    order(l)


def order(l):
    order_list = [
        ["A", "add to order"],
        ["R", "remove from order"],
        ["Q", "quit"]
    ]

    for x in order_list:
        output = "{}: {}".format(x[0], x[1])
        print(output)
    print("-" * 42)
    order_choice = get_string("Please select an option =>")

    if order_choice == "A":
        add_pizza(l)
    elif order_choice == "R":
        remove_pizza(l)
    elif order_choice == "Q":
        print("Thank you for ordering with Papa's Pizzeria!")
        return
    else:
        print("Unrecognised entry must be A or R")
        return order(l)


def add_pizza(l):
    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {:<10} -- ${}".format(i, l[i][0], l[i][1])
        print(output)

    choice = get_integer("Please choose a menu item number =>")
    print("-" * 42)
    # validate, possibly change design later to accommodate word variations
    if -1 < choice < len(l):
        quantity = get_integer("How many {} pizzas would you like to add?".format(l[choice][0]))
        # validate
        l[choice][2] += quantity
        cost_2 = l[choice][1] * quantity
        print("You ordered {} {} pizzas".format(l[choice][2], l[choice][0]))
        print("-" * 42)
        print("Cost is ${}".format(cost_2))
        print("-" * 42)
        ask_again = get_string("Would you like to add another pizza?")
        if ask_again == "Yes":
            return add_pizza(l)
        else:
            return order(l)
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return add_pizza(l)


def remove_pizza(l):

    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${} ".format(i, l[i][2], l[i][0], l[i][1])
        print(output)

    choice = get_integer("Please choose the menu item number that you want to remove=> ")
    print("-" * 42)
    # validate
    if -1 < choice < len(l):
        quantity = get_integer("How many {} pizzas would you like to remove?".format(l[choice][0]))
        print("-" * 42)
        # validate
        l[choice][2] -= quantity
        cost_3 = l[choice][1] * quantity
        print("You  now have {} {} pizzas".format(l[choice][2], l[choice][0]))
        print("-" * 42)
        print("- ${} from your order".format(cost_3))
        return order(l)
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return remove_pizza(l)


def main():
    pizza_list = [
        ["Cheese", 5, 0],
        ["Pepperoni", 5, 0]
    ]

    option_list = [
        ["D", "Delivery"],
        ["P", "Pick-up"],
        ["Q", "Quit"]
    ]
    print("-" * 42)

    run_program = True
    while run_program:
        for x in option_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("-" * 42)
        service = get_string("Select an option =>")
        print("-" * 42)
        if service == "D":
            delivery(pizza_list)
            run_program = False
        elif service == "P":
            pick_up(pizza_list)
            run_program = False
        elif service == "Q":
            print("Thank you for ordering with Papa's Pizzeria!")
            run_program = False
        else:
            print("Unrecognised entry must be P, D or Q")


def intro():
    print("Welcome to Papa's Pizzeria!")


intro()

if __name__ == "__main__":
    main()
