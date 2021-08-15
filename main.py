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
    return phone


def get_integer(m, min_, max_):
    """Integer validation function."""
    # sets minimum and maximum amount of integers
    get_user_integer = True
    while get_user_integer:
        try:
            my_integer = int(input(m))
        except ValueError:
            # repeats until requirements are filled
            print("Please type a valid number")
            continue
        if my_integer < min_:
            print("The value you entered is too low")
            continue
        elif my_integer > max_:
            # returns input if user enters below min or above max
            print("The value you entered is too high")
            continue
        return my_integer


def get_string(m):
    """String validation function."""
    cont = True
    while cont:
        user_input = input(m)
        # allows program to accept upper and lower cases
        user_input = user_input.upper()
        user_input = user_input.strip()
        return user_input


def get_ad(m):
    """Address validation function."""
    get_address = True
    while get_address:
        user_input = input(m)
        # if address is too long or too short returns input
        if len(user_input) > 50:
            print("Invalid Address")
        elif len(user_input) < 5:
            print("Invalid Address")
        else:
            return user_input


def get_name(m):
    """User name validation function."""
    get_names = True
    while get_names:
        user_input = input(m)
        # if name is too long or too short returns input
        if len(user_input) > 25:
            print("Sorry, name is too long")
        elif len(user_input) < 2:
            print("Sorry, name is too short")
        else:
            return user_input


def check_name_present(t, n):
    """Check if a name is already in the pizza list.

     t: order list
     n: choice name
    """
    for i in range(0, len(t)):
        if t[i][0] == n:
            return i
    return -1


def menu_pizza(p):
    """Prints pizza menu with index number.
    :param p: list
    :return: None
    """

    print("⭒" * 53)
    print("{:>8}".format("Menu"))
    print("⭒" * 53)
    print("-" * 60)
    for x in range(0, len(p)):
        output = "{:<2} {:<12} {:>8}{:.2f}".format(x, p[x][0], "$", p[x][1])
        print(output)
    print("-" * 60)
    return


def get_customer_details(o, d, g):
    """Presents delivery/pick up options.
    :param o: list
    :param d: list
    :param g: list
    :return: None
    """

    # if customer details are unfilled, asks user for details
    if len(d) < 1:
        for x in o:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("-" * 60)
        service = get_string("Select an option =>")
        if service == "D":
            delivery(o, d, g)
        elif service == "P":
            pick_up(d)
        else:
            print("Unrecognised entry, must be (P) or (D)")
            return get_customer_details(o, d, g)
    # if customer details are already filled, shows details
    else:
        print("Current Customer details:")
        # prints customer details
        for i in range(0, len(d)):
            output = "{}: {}".format(d[i][0], d[i][1])
            print(output)
        cont = True
        while cont:
            ask = get_string("Do you want to overwrite customer details, (Y) or (N)")
            # if user chooses to overwrite details, clears current information
            if ask == "Y":
                # d is customer details
                d.clear()
                # g is extras (delivery cost)
                g.clear()
                return get_customer_details(o, d, g)
            elif ask == "N":
                return None
            else:
                print("Unrecognisable entry, enter (Y) or (N)")
                continue


def pick_up(d):
    """Get customer details for pick up option.
    :param d:list
    :return:None
    """
    # asks for customer's name and phone number
    order_choice = get_name("What is your name?")
    order_num = get_phone()
    # adds customer details to list
    list_1 = ["Name", order_choice]
    list_2 = ["Number", order_num]
    d.append(list_1)
    d.append(list_2)

    # prints customer details supplied
    for i in range(0, len(d)):
        print("•" * 60)
        output = "{}: {}".format(d[i][0], d[i][1])
        print(output)
    print("•" * 60)
    cont = True
    while cont:
        ask = get_string("Are these details correct, (Y) or (N)")
        print("-" * 60)
        if ask == "Y":
            return None
        elif ask == "N":
            # overwrites customer details and asks for customer details again
            d.clear()
            return pick_up(d)
        else:
            # repeats error message until user selects valid entry
            print("Unrecognizable entry, please select (Y) or (N)")
            continue


def delivery(o, d, g):
    """Get customer details for delivery option.
    :param o: list
    :param d: list
    :param g: list
    :return: None
    """

    # asks user if they are OK with delivery fee, if not returns to main menu
    ask = get_string("Delivery fee of $3 will be charged, (Y) or (N)")
    if ask == "Y":
        # adds delivery cost to extras list
        extra_list = ["extras", 1, 3]
        g.append(extra_list)
        # adds customer details to list
        order_choice = get_name("What is your name?")
        order_num = get_phone()
        ad_num = get_integer("What is your Street Number?", 0, 9999)
        ad_name = get_ad("What is your Street Name?")
        address = "{} {}".format(ad_num, ad_name)
        list_1 = ["Name", order_choice]
        list_2 = ["Number", order_num]
        list_3 = ["Address", address]
        d.append(list_1)
        d.append(list_2)
        d.append(list_3)

        for i in range(0, len(d)):
            print("•" * 60)
            # prints customer details and asks if they are correct
            output = "{}: {}".format(d[i][0], d[i][1])
            print(output)
        print("•" * 60)
        cont = True
        while cont:
            ask = get_string("Are these details correct, (Y) or (N)")
            print("-" * 60)
            if ask == "Y":
                return
            elif ask == "N":
                # overwrites details if details supplied are wrong
                d.clear()
                pick_up(d)
            else:
                # repeats error message until user selects valid entry
                print("Unrecognizable entry, please select (Y) or (N)")
                continue
    elif ask == "N":
        return get_customer_details(o, d, g)
    else:
        # repeats error message until user selects valid entry
        print("Unrecognisable entry, must be (Y) or (N)")
        return delivery(o, d, g)


def new_pizza(t, p):
    """Add a new pizza to the order.
    :param t: list
    :param p: list
    :return: None
    """

    c = 0

    # prints pizza menu with indexes
    for i in range(0, len(p)):
        output = "{:<2} {:<12} {:>8}{:.2f}".format(i, p[i][0], "$", p[i][1])
        print(output)
    print("-" * 60)
    # asks user what pizza they want and if it is not already in the order asks them to add another one
    # if pizza is already in order, redirects to add pizza function
    choice = get_integer("Please choose an option =>", 0, len(p)-1)
    name = p[choice][0]
    checked_name = check_name_present(t, name)

    if checked_name == -1:
        # no problem, proceed as usual
        quantity = get_integer("Please enter a quantity", 0, 5)
        # sets maximum amount of pizzas user can order per pizza type
        if 0 < quantity <= 5:
            # creates new list with the customers pizza order
            new_list = [p[choice][0], quantity, p[choice][1]]
            # multiplies the quantity by pizza cost
            c += quantity * p[choice][1]
            # adds customers pizza order to order list
            t.append(new_list)
            # prints how many and what type of pizza was added to the order
            print("{} {} pizzas have been added to the order".format(quantity, p[choice][0]))
            print("-" * 60)
            return
        elif quantity == 0:
            print("Please enter a number more than 0")
            return new_pizza(t, p)
    else:
        # you already have x  cheese pizzas ordered you can add y more
        output = "You have {} {} pizzas in the order already".format(t[checked_name][1], t[checked_name][0])
        print(output)
        add_pizza(t)
        return None


def edit_order(t, e):
    """Presents editing order option menu.
    :param t: list
    :param e: list
    :return: None
    """
    # only allows function to run if the order list is not empty

    if len(t):
        # prints options for editing order (add pizza, remove pizza)
        for x in e:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("-" * 60)
        order_choice = get_string("Please select an option =>")
        if order_choice == "A":
            add_pizza(t)
            return
        elif order_choice == "R":
            remove_pizza(t)
            return
        else:
            print("Unrecognisable entry, enter A or R")
            return edit_order(t, e)
    else:
        # prints a message if order list is empty
        print("Please add a pizza to the order first")
        print("-" * 60)


def add_pizza(t):
    """Allows user to add a pizza to an existing option in the order list.
    :param t: list
    :return: None
    """
    # print list with indices

    c = 0
    headings = "{} {:>16}".format("Pizza", "Qty")
    print(headings)
    for i in range(0, len(t)):
        output = "{:<2} {:<12} {:>4}{}".format(i, t[i][0], "x", t[i][1])
        print(output)
    # asks user what pizza they want and the quantity
    choice = get_integer("Please choose a menu item number =>", 0, len(t) - 1)
    # if amount of pizzas in order is less than 5, allows user to order more pizzas
    if t[choice][1] < 5:
        quantity = get_integer("How many {} pizzas would you like to add".format(t[choice][0]), 0, 4)
        # adds amount of pizzas to order
        # if there is more than 5 pizzas in order, asks user to re-enter amount
        t[choice][1] += quantity
        if t[choice][1] <= 5:
            # multiplies the quantity by pizza cost
            c += t[choice][1] * t[choice][2]
            print("You added {} {} pizzas".format(quantity, t[choice][0]))
            print("-" * 60)
            return None
        else:
            # minuses pizzas if the amount of pizzas is more than 5
            t[choice][1] -= quantity
            print("Maximum amount of pizzas you can order is 5")
            return add_pizza(t)
    else:
        print("Maximum amount of pizzas you can order is 5")
        return None


def remove_pizza(t):
    """Allows user to remove/delete pizzas from order.
    :param t: list
    :return: None
    """
    # prints customer order with indexes

    c = 0
    headings = "{} {:>16}".format("Pizza", "Qty")
    print(headings)
    for i in range(0, len(t)):
        output = "{:<2} {:<12} {:>4}{}".format(i, t[i][0], "x", t[i][1])
        print(output)

    choice = get_integer("Please choose a menu item number => ", 0, len(t)-1)
    # if the number entered is less than index numbers available, function is returned
    if choice < len(t):
        quantity = get_integer("How many {} pizzas would you like to remove".format(t[choice][0]), 0, 5)
        # amount is removed if less than amount present
        if quantity < t[choice][1]:
            # removes from quantity
            t[choice][1] -= quantity
            # removes from cost
            c -= t[choice][2] * - t[choice][1]
            print("You now have {} {} pizzas".format(t[choice][1], t[choice][0]))
            print("-" * 60)
            return None
        elif quantity >= t[choice][1]:
            # removes pizza from order if quantity is larger or equal to amount available
            print("All {} pizzas have been removed".format(t[choice][0]))
            t.pop(choice)
            return None
    else:
        print("Please enter a number on the menu")
        return remove_pizza(t)


def delete_order(t, d, g):
    """Allows user to fully delete order.
    :param t: list
    :param d: list
    :param g: list
    :return: None
    """
    # if customer details or pizza order contains info, allows function to run
    if len(t) or len(d):
        cont = True
        while cont:
            ask = get_string("Do you want to delete order, (Y) or (N)")
            # clears all current information stored in lists
            if ask == "Y":
                # t is customer order
                t.clear()
                # d is customer details
                d.clear()
                # g is extras
                g.clear()
                print("--------------------🍕Starting Order🍕---------------------")
                return None
            elif ask == "N":
                return None
            else:
                print("Unrecognisable entry, enter (Y) or (N)")
                continue
    else:
        print("Please enter order details")
        print("-" * 60)
        return None


def review_order(t, d, g):
    """Shows user the order, lets the confirm, cancel or delete order.
    :param t: list
    :param d: list
    :param g: list
    :return: None
    """
    # only allows user to review order if order list is filled

    c = 0

    if len(t):
        # prints order list with indexes
        headings = "{:<2} {:>9} {:>13}".format("Qty", "Pizza", "Cost")
        print(headings)
        for i in range(0, len(t)):
            output = "{}{:<6} {:<12} {:>3}{:.2f}".format("x", t[i][1], t[i][0], "$", t[i][2])
            print(output)
            # multiplies cost by quantity
            c += t[i][1] * t[i][2]
        # prints extras list with indexes
        for i in range(0, len(g)):
            output = "{}{:<7} {:<12} {:>3}{:.2f}".format("x", g[i][1], g[i][0], "$", g[i][2])
            print(output)
            # multiplies cost by quantity
            c += g[i][1] * g[i][2]
        # prints total cost
        print("Total cost:   {:>10}{:.2f}".format("$", c))
        print("-" * 60)
        # if customer details list is filled, asks user to confirm order
        if len(d):
            cont = True
            while cont:
                confirm = get_string("Finalise order: (F) or (N), (C) to cancel")
                # if user chooses to confirm, prints customer details
                if confirm == "F":
                    print("⭒" * 53)
                    for i in range(0, len(t)):
                        output = "{}{:<2} {:<12} {:>8}{:.2f}".format("x", t[i][1], t[i][0], "$", t[i][2])
                        print(output)
                    for i in range(0, len(g)):
                        output = "{}{:<2} {:<12} {:>8}{:.2f}".format("x", g[i][1], g[i][0], "$", g[i][2])
                        print(output)
                    print("Total cost:   {:>10}{:.2f}".format("$", c))
                    print("-" * 60)
                    print("Customer Details")
                    print("-" * 60)
                    for i in range(0, len(d)):
                        output = "{}: {}".format(d[i][0], d[i][1])
                        print(output)
                    print("⭒" * 53)
                    run = True
                    while run:
                        ask = get_string("Would you like to confirm your order, (Y) or (N)")
                        if ask == "Y":
                            print("-" * 60)
                            print("Order Complete")
                            print("-" * 60)
                            print("Thank you for ordering with Papa's Pizzeria!")
                            print("--------------------🍕Starting Order🍕---------------------")
                            # clears all information stored in lists
                            t.clear()
                            d.clear()
                            g.clear()
                            return
                        elif ask == "N":
                            return
                        else:
                            print("Unrecognisable entry, must be (Y) or (N)")
                            cont = False
                            continue
                elif confirm == "D":
                    # clears all information stored in lists
                    t.clear()
                    d.clear()
                    g.clear()
                    return
                elif confirm == "N":
                    return
                else:
                    print("Unrecognisable entry, must be (F), (N) or (C)")
                    continue
        else:
            print("Please fill in customer details")
            print("-" * 60)
            return None
    else:
        print("Please add a pizza to the order first")
        print("-" * 60)
        return None


def main():
    """Shows main option menu.
    :return: None
    """
    customer_list = []

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
        ["G", "Get Customer details"],
        ["N", "Add pizza to order"],
        ["E", "Edit order"],
        ["D", "Delete order"],
        ["R", "Review order"],
        ["Q", "Quit"]
    ]

    option_list = [
        ["D", "Delivery"],
        ["P", "Pick-up"]
    ]

    edit_list = [
        ["A", "Add pizza"],
        ["R", "Remove pizza"]
    ]

    customer_details = []

    extras = []

    print("--------------------🍕Starting Order🍕---------------------")
    run_program = True
    while run_program:
        # prints menu options
        for x in order_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        print("-" * 60)
        order_choice = get_string("Please select an option =>")
        print("-" * 60)
        if order_choice == "M":
            menu_pizza(pizza_list)
        elif order_choice == "G":
            get_customer_details(option_list, customer_details, extras)
        elif order_choice == "N":
            new_pizza(customer_list, pizza_list)
        elif order_choice == "E":
            edit_order(customer_list, edit_list)
        elif order_choice == "R":
            review_order(customer_list, customer_details, extras)
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
