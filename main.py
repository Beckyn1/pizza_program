def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def pick_up(d):
    order_choice = get_string("What is your name?")
    order_num = get_integer("What is your phone number?")
    # validate
    new_list = order_choice, order_num
    d.append(new_list)


def delivery(c, d):
    ask = get_string("Deliver fee of $3 will be charged, Y or N?")
    if ask == "Y":
        c += 3
        order_choice = get_string("What is your name?")
        order_num = get_integer("What is your phone number?")
        address = get_string("What is your address?")
        new_list = order_choice, order_num, address
        d.append(new_list)
    elif ask == "N":
        return
    else:
        print("Unrecognisable entry")
        return delivery(c, d)


def add_pizza(l, c):
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
        # multiplies the quantity by pizza cost and adds it to the total cost
        c = (l[choice][1] * l[choice][2]) + c
        print("You ordered {} {} pizzas".format(l[choice][1], l[choice][0]))
        print("-" * 42)
        print("Total cost is ${}".format(c))
        print("-" * 42)
        ask_again = get_string("Would you like to add another pizza?")
        if ask_again == "Yes":
            return add_pizza(l, c)
        else:
            return
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return add_pizza(l, c)


def subtract_pizza(l, c):

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
        cost = c - (l[choice][2] * - l[choice][1])
        print("You  now have {} {} pizzas".format(l[choice][1], l[choice][0]))
        print("-" * 42)
        print("Total cost is ${}".format(cost))
        print("-" * 42)
        return
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return subtract_pizza(l, c)


def new_pizza(l, c, p):
    for i in range(0, len(p)):
        output = "{}: {:<10} -- ${} ".format(i, p[i][0], p[i][1])
        print(output)

    # validate entries
    choice = get_integer("Please choose a menu item number =>")
    if -1 < choice < len(p):
        quantity = get_integer("Please enter a quantity")
        # sets all pizza costs to $5
        cost = 5
        name = p[choice][0]
        new_list = [name, quantity, cost]
        # adds cost of pizzas to total cost
        c = cost * quantity
        l.append(new_list)
        print("{} {} pizzas -- ${} have been added to the order".format(quantity, name, cost))
        print("-" * 42)
        print("Total cost is ${}".format(c))
        print("-" * 42)
        return
    else:
        print("Unrecognisable entry")
        return new_pizza(l, c, p)


def delete_pizza(l):
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${} ".format(i, l[i][1], l[i][0], l[i][2])
        print(output)

    remove = get_integer("Which pizza type do you want to delete?")
    if -1 < remove < len(l):
        l.pop(remove)
        print("{} is removed".format(remove))
        return
    else:
        print("Unrecognisable entry, must be a number in the menu list")
        return delete_pizza(l)


def get_order_details(o, c, d):
    print("Welcome to Papa's Pizzeria")
    print("-" * 42)
    for x in o:
        output = "{}: {}".format(x[0], x[1])
        print(output)
        print("-" * 42)
    service = get_string("Select an option =>")
    print("-" * 42)
    if service == "D":
        delivery(c, d)
    elif service == "P":
        pick_up(d)
    else:
        print("Unrecognised entry must be P or D")
        return get_order_details(o, c, d)


def menu_pizza(p):
    for x in p:
        output = "{}: ${}".format(x[0], x[1])
        print(output)
    return


def review_order(l, c, d):
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${}".format(i, l[i][1], l[i][0], l[i][2])
        print(output)
        c = (l[i][1] * l[i][2])
    print("Total cost is ${}".format(c))
    confirm = get_string("Confirm Order?")
    if confirm == "Yes":
        print("Your total cost is ${}".format(c))
        print("-" * 42)
        for x in d:
            print("Order Details:")
            print("Name: Address: Phone No:")
            output = "{}: {} --- {}".format(x[0], x[1], x[2])
            print(output)
        print("Thank you for ordering with Papa's Pizzeria!")
        print("---Starting New Order---")
        return main()
    else:
        return


def main():
    customer_list = []

    cost = 0

    pizza_list = [
        ["Cheese", 5],
        ["Pepperoni", 5],
        ["Hawaiian", 5],
        ["Meatlovers", 5]
    ]

    order_list = [
        ["M", "Menu"],
        ["D", "delete pizza type"],
        ["A", "add to order"],
        ["S", "subtract from order"],
        ["R", "review order"],
        ["Q", "quit"]
    ]

    option_list = [
        ["D", "Delivery"],
        ["P", "Pick-up"]
    ]

    customer_details = []

    # print welcome message
    # call the function to get customer details
    get_order_details(option_list, cost, customer_details)
    print("---Starting Order---")
    new_pizza(customer_list, cost, pizza_list)

    run_program = True
    while run_program:
        for x in order_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        order_choice = get_string("Please select an option =>")
        print("-" * 42)
        if order_choice == "M":
            menu_pizza(pizza_list)
        elif order_choice == "A":
            add_pizza(customer_list, cost)
        elif order_choice == "S":
            subtract_pizza(customer_list, cost)
        elif order_choice == "D":
            delete_pizza(customer_list)
        elif order_choice == "R":
            review_order(customer_list, cost, customer_details)
        elif order_choice == "Q":
            print("Thank you for choosing Papa's Pizzeria!")
            return None
        else:
            print("Unrecognised entry must be A or R")


if __name__ == "__main__":
    main()