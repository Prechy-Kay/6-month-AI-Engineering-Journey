for order in range(1, 11):
    if order < 4 and order % 2 == 0:
        print("Order", order, "Even Small")
    elif order < 7 and order % 2 == 0: 
        print("Order", order, "Even Medium")
    elif order < 11 and order % 2 == 0: 
        print("Order", order, "Even Large")
    else:
        print("Order", order, "Odd order")
