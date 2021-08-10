# ask about pizza already in list
# ask about popping showing name still
# ask about result thing

def get_integer(m, min=0, max=9999999):
    # sets minimum and maximum amount of integers
    get_user_integer = True
    while get_user_integer:
        try:
            user_input = int(input(m))
        except ValueError:
            # if user enters anything that isn't a integer it repeats till they fill the requirements
            print("Please type a number")
            continue

        if user_input < min or user_input > max:
            # returns input if user enters below min or above max
            print("Please type a number")
            continue
        get_user_integer = False
    return user_input


def get_string(m):
    user_input = input(m)
    # allows program to accept upper and lower cases
    user_input = user_input.upper()
    user_input = user_input.strip()
    return user_input


def get_ad(m):
    get_address = True
    while get_address is True:
        user_input = input(m)
        # if address is too long or too short returns input
        if len(user_input) > 50:
            print("Name is too long")
        elif len(user_input) < 2:
            print("Name is too short")
        else:
            return user_input


def get_name(m):
    get_names = True
    while get_names is True:
        user_input = input(m)
        # if name is too long or too short returns input
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
            # if user does not enter an integer returns input
            print("Please enter your phone number")
            continue
        # returns input if phone number is less than min or more than mix
        if min < user_input < max:
            # repeats error message until user selects valid entry
            print("Phone number is not correct")
            continue
        get_number = False
    return user_input


def check_name_present(p, t):
    for i in range(0, len(p)):
        if p[i][0] == t[i][0]:
            print("test")
    return


def menu_pizza(p):
    # prints pizza menu with index number
    for x in p:
        output = "{}: ${:.2f}".format(x[0], x[1])
        print(output)
    return


def pick_up(d):
    # asks for customer's name and phone number
    order_choice = get_name("What is your name?")
    order_num = get_num("What is your phone number?")
    # adds customer details to list
    list_1 = ["Name", order_choice]
    list_2 = ["Number", order_num]
    d.append(list_1)
    d.append(list_2)

    # prints customer details supplied
    for i in range(0, len(d)):
        print("-" * 42)
        output = "{}: {}".format(d[i][0], d[i][1])
        print(output)
    print("-" * 42)
    cont = True
    while cont:
        ask = get_string("Are these details correct, Y or N")
        if ask == "Y":
            return
        elif ask == "N":
            # overwrites customer details and asks for customer details again
            d.clear()
            return pick_up(d)
        else:
            # repeats error message until user selects valid entry
            print("Unrecognizable entry, please select Y or N")
            continue


def delivery(c, d, g):
    # asks user if they are OK with delivery fee, if not returns to main menu
    ask = get_string("Delivery fee of $3 will be charged, Y or N?")
    if ask == "Y":
        # adds delivery cost to extras list
        extra_list = ["extras", 1, 3]
        g.append(extra_list)
        # adds customer details to list
        order_choice = get_name("What is your name?")
        order_num = get_num("What is your phone number?")
        address = get_ad("What is your address?")
        list_1 = ["Name", order_choice]
        list_2 = ["Number", order_num]
        list_3 = ["Address", address]
        d.append(list_1)
        d.append(list_2)
        d.append(list_3)

        for i in range(0, len(d)):
            print("-" * 42)
            # prints customer details and asks if they are correct
            output = "{}: {}".format(d[i][0], d[i][1])
            print(output)
        print("-" * 42)
        cont = True
        while cont:
            ask = get_string("Are these details correct, Y or N")
            if ask == "Y":
                return
            elif ask == "N":
                # overwrites details if details supplied are wrong
                d.clear()
                pick_up(d)
            else:
                # repeats error message until user selects valid entry
                print("Unrecognizable entry, please select Y or N")
                continue
    elif ask == "N":
        return
    else:
        # repeats error message until user selects valid entry
        print("Unrecognisable entry, must be Y or N")
        return delivery(c, d, g)


def new_pizza(t, c, p):
    # prints pizza menu with indexes
    for i in range(0, len(p)):
        output = "{}: {:<10} -- ${:.2f} ".format(i, p[i][0], p[i][1])
        print(output)
    # asks user what pizza they want and if it is not already in the order asks them to add another one
    # if pizza is already in order, redirects to add pizza function
    choice = get_integer("Please choose a menu item number =>")
   # if check_name_present(p, t):
        # function that adds a pizza to an already existing pizza in the order
        # add_pizza(t, c)
    # elif not check_name_present(p, t):
    if choice < len(p):
        quantity = get_integer("Please enter a quantity")
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
            print("-" * 42)
            return
        elif quantity == 0:
            print("Please enter a number more than 0")
            return new_pizza(t, c, p)
        else:
            print("Maximum amount of pizzas you can order is 5")
            return new_pizza(t, c, p)
    else:
        print("please enter a number in the menu")
        return new_pizza(t, c, p)


def edit_order(t, c, e):
    # only allows function to run if the order list is not empty
    if len(t):
        # prints options for editing order (add pizza, remove pizza)
        for x in e:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        order_choice = get_string("Please select an option =>")
        if order_choice == "A":
            add_pizza(t, c)
            return
        elif order_choice == "R":
            remove_pizza(t, c)
            return
        else:
            print("Unrecognisable entry, enter A or R")
            return order_choice
    else:
        # prints a message if order list is empty
        print("Please add a pizza to the order first")
        print("-" * 42)


def add_pizza(t, c):
    # print list with indexes
    for i in range(0, len(t)):
        output = "{}: {} {:<10} -- ${:.2f}".format(i, t[i][1], t[i][0], t[i][2])
        print(output)
    # asks user what pizza they want and the quantity
    choice = get_integer("Please choose a menu item number =>")
    if choice < len(t):
        cont = True
        while cont:
            # if amount of pizzas in order is less than 5, allows user to order more pizzas
            if t[choice][1] < 5:
                quantity = get_integer("how many {} pizzas would you like to add".format(t[choice][0]))
                cont = True
                while cont:
                    # adds amount of pizzas to order
                    # if there is more than 5 pizzas in order, asks user to re-enter amount
                    t[choice][1] += quantity
                    if t[choice][1] <= 5:
                        # multiplies the quantity by pizza cost
                        c += t[choice][1] * t[choice][2]
                        print("You added {} {} pizzas".format(quantity, t[choice][0]))
                        print("-" * 42)
                        return
                    else:
                        # minuses pizzas if the amount of pizzas is more than 5
                        t[choice][1] -= quantity
                        print("Maximum amount of pizzas you can order is 5")
                        return add_pizza(t, c)
            else:
                print("Maximum amount of pizzas you can order is 5")
                return add_pizza(t, c)
    else:
        # returns if user enters number not in index
        print("please enter a number on the menu")
        return add_pizza(t, c)


def remove_pizza(t, c):
    # prints customer order with indexes
    for i in range(0, len(t)):
        output = "{}: {} {:<10} -- ${:.2f}".format(i, t[i][1], t[i][0], t[i][2])
        print(output)

        choice = get_integer("Please choose a menu item number => ")
        # if the number entered is less than index numbers available, function is returned
        if choice < len(t):
            quantity = get_integer("how many {} pizzas would you like to remove".format(t[choice][0]))
            # amount is removed if less than amount present
            if quantity < t[i][1]:
                # removes from quantity
                t[choice][1] -= quantity
                # removes from cost
                c -= t[choice][2] * - t[choice][1]
                print("You  now have {} {} pizzas".format(t[choice][1], t[choice][0]))
                print("-" * 42)
                return
            elif quantity >= t[i][1]:
                # removes pizza from order if quantity is larger than amount available
                t.pop(choice)
                print("{} has been removed".format(choice))
                return
        else:
            print("please enter a number on the menu")
            return remove_pizza(t, c)


def get_customer_details(o, c, d, g):
    # if customer details are unfilled, asks user for details
    if len(d) < 1:
        for x in o:
            output = "{}: {}".format(x[0], x[1])
            print(output)
            print("-" * 42)
        service = get_string("Select an option =>")
        print("-" * 42)
        if service == "D":
            delivery(c, d, g)
        elif service == "P":
            pick_up(d)
        else:
            print("Unrecognised entry must be P or D")
            return get_customer_details(o, c, d, g)
    # if customer details are already filled, shows details
    else:
        print("Current Customer details:")
        # prints customer details
        for i in range(0, len(d)):
            output = "{}: {}".format(d[i][0], d[i][1])
            print(output)
        cont = True
        while cont:
            ask = get_string("Do you want to overwrite customer details, Y or N?")
            # if user chooses to overwrite details, clears current information
            if ask == "Y":
                # d is customer details
                d.clear()
                # g is extras (delivery cost)
                g.clear()
                return get_customer_details(o, c, d, g)
            elif ask == "N":
                return
            else:
                print("Unrecognisable entry, enter Y or N")
                continue


def delete_order(t, d, g):
    # if customer details or pizza order contains info, allows function to run
    if len(t) or len(d):
        cont = True
        while cont:
            ask = get_string("Do you want to delete order, Y or N?")
            # clears all current information stored in lists
            if ask == "Y":
                # t is customer order
                t.clear()
                # d is customer details
                d.clear()
                # g is extras
                g.clear()
                print("---Starting New Order---")
                return
            elif ask == "N":
                return
            else:
                print("Unrecognisable entry, enter Y or N")
                continue


def review_order(t, c, d, g):
    # only allows user to review order if order list is filled
    if len(t):
        # prints order list with indexes
        for i in range(0, len(t)):
            output = "{} {:<10} -- ${:.2f}".format(t[i][1], t[i][0], t[i][2])
            print(output)
            # multiplies cost by quantity
            c += t[i][1] * t[i][2]
        # prints extras list with indexes
        for i in range(0, len(g)):
            output = "{} {:<10} -- ${:.2f}".format(g[i][1], g[i][0], g[i][2])
            print(output)
            # multiplies cost by quantity
            c += g[i][1] * g[i][2]
        # prints total cost
        print("Total cost is ${:.2f}".format(c))
        print("-" * 42)
        # if customer details list is filled, asks user to confirm order
        if len(d):
            cont = True
            while cont:
                confirm = get_string("Confirm order: (Y) or (N), (D) to cancel")
                # if user chooses to confirm, prints customer details
                if confirm == "Y":
                    print("Your total cost is ${:.2f}".format(c))
                    print("-" * 42)
                    for i in range(0, len(d)):
                        output = "{}: {}".format(d[i][0], d[i][1])
                        print(output)
                    print("Thank you for ordering with Papa's Pizzeria!")
                    print("---Starting New Order---")
                    # clears all information stored in lists
                    t.clear()
                    d.clear()
                    g.clear()
                    return "Complete"
                elif confirm == "D":
                    # clears all information stored in lists
                    t.clear()
                    d.clear()
                    g.clear()
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
        ["A", "add pizza"],
        ["R", "remove pizza"]
    ]

    customer_details = []

    extras = []

    print("---Starting Order---")
    run_program = True
    while run_program:
        # prints menu options
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
