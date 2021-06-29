def get_integer(m):
    user_input = int(input(m))
    return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def add_pizza(l):
    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {:<10} -- ${}".format(i, l[i][0], l[i][1])
        print(output)

    choice = get_integer("Please choose a menu item number =>")
    # validate
    if -1 < choice < len(l):
        quantity = get_integer("how many {} pizzas would you like to add".format(l[choice][0]))
        # validate
        l[choice][2] += quantity
        l[choice][1] = l[choice][1] * quantity
        print("You  now have {} {} pizzas".format(l[choice][2], l[choice][0]))
        print("Total is ${}".format(l[choice][1]))
        ask_again = get_string("Would you like to add another pizza?")
        if ask_again == "Yes":
            return add_pizza(l)
        else:
            return delivery(l)
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return add_pizza(l)


def remove_pizza(l):

    # print list with indexes
    for i in range(0, len(l)):
        output = "{}: {:<10} -- ${} ".format(i, l[i][0], l[i][1])
        print(output)

    choice = get_integer("Please choose a menu item number => ")
    # validate
    if -1 < choice < len(l):
        print("{} is chosen".format(l[choice][0]))
        quantity = get_integer("how many {} pizzas would you like to remove".format(l[choice][0]))
        # validate
        l[choice][2] -= quantity
        print("You  now have {} {} pizzas".format(l[choice][2], l[choice][0]))
    else:
        print("Unrecognised entry, can only be be a number on the list")
        return remove_pizza(l)


def delivery(l):
    order_list = [
        ["A", "add to order"],
        ["R", "remove from order"],
        ["Q", "quit"]
    ]
    for x in order_list:
        output = "{}: {}".format(x[0], x[1])
        print(output)

    order = get_string("Select an option =>")
    test = True
    while test:
        if order == "A":
            add_pizza(l)
        elif order == "R":
            remove_pizza(l)
        elif order == "Q":
            return None
        else:
            print("Unrecognised entry must be A, R or Q")
            return delivery(l)

def main():
    pizza_list = [
        ["Cheese", 5, 0],
        ["Pepperoni", 5, 0]
    ]

    delivery(pizza_list)

main()