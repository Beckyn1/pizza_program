# ask about pizza already in list

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


def check_name_present(t, p):
    for i in range(0, len(p)):
        if p[i][0] in t:
            print("{} is already present at index number {}".format(t, i))
            return i
    return -1


def new_pizza(t, c, p):
    for i in range(0, len(p)):
        output = "{}: {:<10} -- ${:.2f} ".format(i, p[i][0], p[i][1])
        print(output)

    choice = get_integer("Please choose a menu item number =>")

    if choice <= len(p):
        quantity = get_integer("Please enter a quantity")
        if quantity <= 5:
            new_list = [p[choice][0], quantity, p[choice][1]]
            c += quantity * p[choice][1]
            # adds cost of pizzas together
            t.append(new_list)
            print("{} {} pizzas -- ${:.2f} have been added to the order".format(quantity, p[choice][0], p[choice][1]))
            print("-" * 42)
            print("Cost is ${:.2f}".format(c))
            print("-" * 42)
            return


def add_pizza(t, c):
    # print list with indexes
    for i in range(0, len(t)):
        output = "{}: {} {:<10} -- ${:.2f}".format(i, t[i][1], t[i][0], t[i][2])
        print(output)
        choice = get_integer("Please choose a menu item number =>")
        quantity = get_integer("how many {} pizzas would you like to add".format(t[choice][0]))
        cont = True
        while cont:
            if quantity <= 5:
                t[choice][1] += quantity
                # multiplies the quantity by pizza cost and adds it to the total cost
                c += t[choice][1] * t[choice][2]
                print("You added {} {} pizzas".format(quantity, t[choice][0]))
                print("-" * 42)
                print("Cost is ${:.2f}".format(c))
                print("-" * 42)
                return
            else:
                print("Maximum amount of pizzas you can order is 5")
                continue


def review_order(t, c, d, g):
    if len(t):
        for i in range(0, len(t)):
            output = "{} {:<10} -- ${:.2f}".format(t[i][1], t[i][0], t[i][2])
            print(output)

            c += t[i][1] * t[i][2]

        for i in range(0, len(g)):
            output = "{} {:<10} -- ${:.2f}".format(g[i][1], g[i][0], g[i][2])
            print(output)

            c += g[i][1] * g[i][2]

        print("Total cost is ${:.2f}".format(c))
        if len(d):
            cont = True
            while cont:
                confirm = get_string("Confirm order: Y or N, D to cancel")
                if confirm == "Y":
                    print("Your total cost is ${:.2f}".format(c))
                    print("-" * 42)
                    for i in range(0, len(d)):
                        output = "{}: {}".format(d[i][0], d[i][1])
                        print(output)
                    print("Thank you for ordering with Papa's Pizzeria!")
                    print("---Starting New Order---")
                    t.clear()
                    d.clear()
                    g.clear()
                    return "Complete"
                elif confirm == "D":
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
