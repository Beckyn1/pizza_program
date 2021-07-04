def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def pick_up(l):
    order_choice = get_string("What is your name?")
    order_num = get_integer("What is your phone number?")
    # validate
    new_list = order_choice, order_num


def delivery(l):
    ask = get_string("Deliver fee of $3 will be charged, is this OK?")

    if ask == "Yes":
        order_choice = get_string("What is your name?")
        order_num = get_integer("What is your phone number?")
        address = get_string("What is your address?")
        new_list = order_choice, order_num, address

    elif ask == "No":
        return main()
    else:
        print("Unrecognisable blah")
        return delivery(l)


def add_pizza(l, c, o, p):
    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${}".format(i, l[i][1], l[i][0], l[i][2])
        print(output)

    choice = get_integer("Please choose a menu item number =>")
    # validate
    if -1 < choice < len(l):
        quantity = get_integer("how many {} pizzas would you like to add".format(l[choice][0]))
        # validate
        l[choice][1] += quantity
        c = c + (l[choice][2] * quantity)
        print("You ordered {} {} pizzas".format(l[choice][1], l[choice][0]))
        print("-" * 42)
        print("Total cost is ${}".format(c))
        print("-" * 42)
        ask_again = get_string("Would you like to add another pizza?")
        if ask_again == "Yes":
            return add_pizza(l, c, o, p)
        else:
            return order(l, c, o, p)
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return add_pizza(l, c, o, p)


def subtract_pizza(l, c, o, p):

    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${}".format(i, l[i][1], l[i][0], l[i][2])
        print(output)
    # print list with indexes
    # print list with indexes
    choice = get_integer("Please choose a menu item number => ")
    # validate
    if -1 < choice < len(l):
        quantity = get_integer("how many {} pizzas would you like to remove".format(l[choice][0]))
        # validate
        l[choice][1] -= quantity
        c = c - (l[choice][2] * quantity)
        print("You  now have {} {} pizzas".format(l[choice][1], l[choice][0]))
        print("-" * 42)
        print("Total cost is ${}".format(c))
        return order(l, c, o, p)
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return subtract_pizza(l, c, o, p)


def new_pizza(l, c, o, p):
    for i in range(0, len(l)):
        output = "{}: {:<10} -- ${} ".format(i, l[i][0], l[i][2])
        print(output)

    new_pizzas = get_integer("Please enter a new index number")

    if new_pizzas in range(0, len(l)):
        return add_pizza(l, c, o, p)
    else:
        # validate entries
        name = get_string("Please enter a pizza name")
        cost = get_integer("Please enter a cost")
        quantity = 0
        new_list = [name, quantity, cost]
        l.append(new_list)
        print("{} -- ${} has been added to the menu".format(name, cost))
        return order(l, c, o, p)


def delete_pizza(l, c, o, p):
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${} ".format(i, l[i][1], l[i][0], l[i][2])
        print(output)

    remove = get_integer("Which pizza type do you want to delete?")
    if -1 < remove < len(l):
        l.pop(remove)
        print("{} is removed".format(remove))
        return order(l, c, o, p)
    else:
        print("Unrecognisable entry")
        return delete_pizza(l, c, o, p)


def get_order_details(o,l):

    print("-" * 42)
    for x in o:
        output = "{}: {}".format(x[0], x[1])
        print(output)
        print("-" * 42)
    service = get_string("Select an option =>")
    print("-" * 42)
    if service == "D":
        delivery(l)
        run_program = False
    elif service == "P":
        pick_up(o)
        run_program = False
    elif service == "Q":
        print("Thank you for ordering with Papa's Pizzeria!")
        run_program = False
    else:
        print("Unrecognised entry must be P, D or Q")


def menu_pizza(l, c, o, p):
    for i in range(len(p)):
        print("{}: ${}".format(p[i][0], p[i][1]))
        return order(l, c, o, p)


def order(l, c, o, p):

    for x in o:
        output = "{}: {}".format(x[0], x[1])
        print(output)
    print("-" * 42)
    order_choice = get_string("Please select an option =>")
    if order_choice == "M":
        menu_pizza(l, c, o, p)
    elif order_choice == "A":
        add_pizza(l, c, o, p)
    elif order_choice == "S":
        subtract_pizza(l, c, o, p)
    elif order_choice == "N":
        new_pizza(l, c, o, p)
    elif order_choice == "D":
        delete_pizza(l, c, o, p)
    elif order_choice == "O":
        get_order_details(l, c, o, p)
    elif order_choice == "R":
        review_order(l, c, o, p)
    elif order_choice == "Q":
        print("Thank you for ordering with Papa's Pizzeria!")
        return
    else:
        print("Unrecognised entry must be A, R, N, D, O or Q")
        return order(l, c, o, p)


def review_order(l, c, o, p):
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${}".format(i, l[i][1], l[i][0], l[i][2])
        print(output)
    print("Total cost is ${}".format(c))
    confirm = get_string("Confirm Order?")
    if confirm == "Yes":
        print("Your total cost is ${}".format(c))
        print("Thank you for ordering with Papa's Pizzeria!")
        print("---Starting New Order---")
        return main()
    else:
        return order(l, c, o, p)


def main():
    customer_list = [
        ["Cheese", 0, 5],
        ["Pepperoni", 0, 5],
        ["Hawaiian", 0, 5],
        ["Meatlovers", 0, 5]
    ]

    pizza_list = [
        ["Cheese", 5],
        ["Pepperoni", 5],
        ["Hawaiian", 5],
        ["Meatlovers", 5]
    ]

    cost = 0

    order_list = [
        ["M", "Menu"],
        ["A", "add to order"],
        ["S", "subtract from order"],
        ["N", "add new pizza type"],
        ["D", "delete pizza type"],
        ["R", "review order"],
        ["Q", "quit"]
    ]

    option_list = [
        ["D", "Delivery"],
        ["P", "Pick-up"],
        ["Q", "Quit"]
    ]

    # print welcome message
    # call the functionto get customer details
    # get_order_details(option_list)
    run_program = True
    while run_program:
        for x in order_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("-" * 42)
        order_choice = get_string("Please select an option =>")
        if order_choice == "M":
            menu_pizza(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "A":
            add_pizza(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "S":
            subtract_pizza(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "N":
            new_pizza(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "D":
            delete_pizza(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "O":
            get_order_details(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "R":
            review_order(customer_list, cost, order_list, pizza_list)
            run_program = False
        elif order_choice == "Q":
            print("Thank you for choosing Papa's Pizzeria!")
            run_program = False
        else:
            print("Unrecognised entry must be A or R")


if __name__ == "__main__":
    main()
