def get_integer(m, min=0, max=9999999):
    get_user_integer = True
    while get_user_integer:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please type a number: ->")
            continue

        if user_input < min or user_input > max:
            print("Please type a number: ->")
            continue
        get_user_integer = False
    return user_input


def get_string(m):
    user_input = input(m)
    user_input = user_input.upper()
    user_input = user_input.strip()
    return user_input


def get_ad(m):
    get_address = True
    while get_address is True:
        user_input = input(m)
        if len(user_input) > 50:
            print("Sorry name is too long")
        elif len(user_input) < 2:
            print("sorry name is too short")
        else:
            return user_input


def get_name(m):
    get_names = True
    while get_names is True:
        user_input = input(m)
        if len(user_input) > 25:
            print("Sorry name is too long")
        elif len(user_input) < 2:
            print("sorry name is too short")
        else:
            return user_input


def get_num(m, min=9, max=11):
    get_number = True
    while get_number:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please enter your phone number")
            continue

        if min < user_input < max:
            print("Phone number is not correct")
            continue
        get_number = False
    return user_input


def menu_pizza(p):
    for x in p:
        output = "{}: ${}".format(x[0], x[1])
        print(output)
    return


def pick_up(d):
    order_choice = get_name("What is your name?")
    order_num = get_num("What is your phone number?")
    # validate
    list_1 = ["Name", order_choice]
    list_2 = ["Number", order_num]
    d.append(list_1)
    d.append(list_2)


# try removing cost from all functions except for delivery
def delivery(c, d, e):
    ask = get_string("Delivery fee of $3 will be charged, Y or N?")
    if ask == "Y":
        extra_list = ["extras", 1, 3]
        e.append(extra_list)
        order_choice = get_name("What is your name?")
        order_num = get_num("What is your phone number?")
        address = get_ad("What is your address?")
        list_1 = ["Name", order_choice]
        list_2 = ["Number", order_num]
        list_3 = ["Address", address]
        d.append(list_1)
        d.append(list_2)
        d.append(list_3)
        return
    elif ask == "N":
        return
    else:
        print("Unrecognisable entry")
        return delivery(c, d, e)


def new_pizza(l, c, p):
    for i in range(0, len(p)):
        output = "{}: {:<10} -- ${} ".format(i, p[i][0], p[i][1])
        print(output)

    choice = get_integer("Please choose a menu item number =>")
    if choice <= len(p):
        quantity = get_integer("Please enter a quantity")
        if quantity <= 5:
            new_list = [p[choice][0], quantity, p[choice][1]]
            c += quantity * p[choice][1]
            # adds cost of pizzas together
            l.append(new_list)
            print("{} {} pizzas -- ${} have been added to the order".format(quantity, p[choice][0], p[choice][1]))
            print("-" * 42)
            print("Cost is ${}".format(c))
            print("-" * 42)
            return


def edit_order(l, c, e):
    if len(l):
        for x in e:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        order_choice = get_string("Please select an option =>")
        if order_choice == "A":
            add_pizza(l, c)
            return
        elif order_choice == "R":
            remove_pizza(l, c)
            return
        else:
            print("Unrecognisable entry, enter A or R")
            return order_choice
    else:
        print("Please add a pizza to the order first")
        print("-" * 42)


def add_pizza(l, c):
    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${}".format(i, l[i][1], l[i][0], l[i][2])
        print(output)
        choice = get_integer("Please choose a menu item number =>")
        quantity = get_integer("how many {} pizzas would you like to add".format(l[choice][0]))
        if l[i][1] < 5:
            if quantity <= 5:
                l[choice][1] += quantity
                # multiplies the quantity by pizza cost and adds it to the total cost
                c += l[choice][1] * l[choice][2]
                print("You added {} {} pizzas".format(quantity, l[choice][0]))
                print("-" * 42)
                print("Cost is ${}".format(c))
                print("-" * 42)
                return
            else:
                print("too many pizzas order less")
                return
        else:
            print("too many pizzas order less")
            return


def remove_pizza(l, c):
    for i in range(0, len(l)):
        output = "{}: {} {:<10} -- ${}".format(i, l[i][1], l[i][0], l[i][2])
        print(output)
        # print list with indexes
        # print list with indexes
        choice = get_integer("Please choose a menu item number => ")
        # validate
        quantity = get_integer("how many {} pizzas would you like to remove".format(l[choice][0]))
        # validate
        if quantity < l[i][1]:
            l[choice][1] -= quantity
            c -= l[choice][2] * - l[choice][1]
            print("You  now have {} {} pizzas".format(l[choice][1], l[choice][0]))
            print("-" * 42)
            print("Cost is ${}".format(c))
            print("-" * 42)
            return
        elif quantity >= l[i][1]:
            l.pop(choice)
            print("{} has been removed".format(choice))
            return
        else:
            return remove_pizza(l, c)


def get_customer_details(o, c, d, e):
    if len(d) < 1:
        for x in o:
            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("-" * 42)
        service = get_string("Select an option =>")
        print("-" * 42)
        if service == "D":
            delivery(c, d, e)
        elif service == "P":
            pick_up(d)
        else:
            print("Unrecognised entry must be P or D")
            return get_customer_details(o, c, d, e)
    else:
        print("Current Customer details:")
        for i in range(0, len(d)):
            output = "{}: {}".format(d[i][0], d[i][1])
            print(output)
        ask = get_string("Do you want to overwrite customer details, Y or N?")
        if ask == "Y":
            return get_customer_details(o, c, d, e)
        elif ask == "N":
            return
        else:
            print("Unrecognisable entry, enter Y or N")
            return get_string


def delete_order(l, d, e):
    if len(l) or len(d):
        cont = True
        while cont:
            ask = get_string("Do you want to delete order, Y or N?")
            if ask == "Y":
                l.clear()
                d.clear()
                e.clear()
                print("---Starting New Order---")
                return
            elif ask == "N":
                return
            else:
                print("Unrecognisable entry, enter Y or N")
                continue


def review_order(l, c, d, e):
    if len(l):
        for i in range(0, len(l)):
            output = "{} {:<10} -- ${}".format(l[i][1], l[i][0], l[i][2])
            print(output)
            for y in range(0, len(e)):
                output = "{} {:<10} -- ${}".format(e[y][1], e[y][0], e[y][2])
                print(output)
                c += l[i][1] * l[i][2] + e[y][2]

        print("Total cost is ${}".format(c))
        if len(d):
            cont = True
            while cont:
                confirm = get_string("Confirm or cancel Order, Y, C or N?")
                if confirm == "Y":
                    print("Your total cost is ${}".format(c))
                    print("-" * 42)
                    for i in range(0, len(d)):
                        output = "{}: {}".format(d[i][0], d[i][1])
                        print(output)
                    print("Thank you for ordering with Papa's Pizzeria!")
                    print("---Starting New Order---")
                    l.clear()
                    d.clear()
                    e.clear()
                    return "Complete"
                elif confirm == "C":
                    l.clear()
                    d.clear()
                    e.clear()
                    return
                elif confirm == "N":
                    return
                else:
                    print("Unrecognisable entry, must be Y, C or N")
                    continue
        else:
            print("Please fill in customer details")
    else:
        print("Please add a pizza to the order first")
        print("-" * 42)


def main():
    customer_list = []

    cost = 0

    pizza_list = [
        ["Cheese", 18.50],
        ["Pepperoni", 18.50],
        ["Hawaiian", 18.50],
        ["Meatlovers", 18.50],
        ["Ham & Cheese", 18.50],
        ["Cheez Nuts", 18.50],
        ["Sushi", 18.50],
        ["KimCheesy", 25.50],
        ["Titan Food", 25.50],
        ["Bat", 25.50]
    ]

    order_list = [
        ["M", "Menu"],
        ["G", "get customer details"],
        ["N", "add pizza to order"],
        ["E", "edit order"],
        ["D", "Delete order"],
        ["R", "review order"],
        ["Q", "quit"]
    ]

    option_list = [
        ["D", "Delivery"],
        ["P", "Pick-up"]
    ]

    edit_list = [
        ["A", "add pizza"],
        ["R", "remove pizza"]
    ]

    customer_details = []

    extras = []

    # print welcome message
    # call the function to get customer details
    print("---Starting Order---")
    run_program = True
    while run_program:
        for x in order_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        order_choice = get_string("Please select an option =>")
        print("-" * 42)
        if order_choice == "M":
            menu_pizza(pizza_list)
        elif order_choice == "G":
            get_customer_details(option_list, cost, customer_details, extras)
        elif order_choice == "N":
            new_pizza(customer_list, cost, pizza_list)
        elif order_choice == "E":
            edit_order(customer_list, cost, edit_list)
        elif order_choice == "R":
            result = review_order(customer_list, cost, customer_details, extras)
        elif order_choice == "D":
            delete_order(customer_list, customer_details, extras)
        elif order_choice == "Q":
            print("Thank you for choosing Papa's Pizzeria!")
            return None
        else:
            print("Unrecognised entry must be option in menu list")
            continue


if __name__ == "__main__":
    main()
