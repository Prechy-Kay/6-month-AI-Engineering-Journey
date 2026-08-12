orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
for order in orders:
    if order == "Cake":
        print(order, "requires decoration")
    else:
        print(order, "is ready")



orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
for order in orders:
    if order == "Cake":
        print(order, "requires decoration")
    elif order == "Meat Pie":
        print(order, "requires decoration")
    else:
        print(order, "is ready")



orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
for order in orders:
    if order == "Cake":
        print(order, "is a special order")
    elif order == "Cupcake":
        print(order, "is a small order")
    else:
        print("Regular order")






orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
for order in orders:
    if order == "Cake":
        print(order, "Decorate the cake")
    elif order == "Cupcake":
        print(order, "Pack in a box")
    elif order == "Bread":
        print(order, "Put in a bread bag")
    else:
        print("Pack in a paper bag")





orders = ["Cake", "Bread", "Cupcake", "Meat Pie", "Cake"]
for order in orders:     # Loop over values
    if order == "Cake":
        print(order, "Decorate")
    elif order == "Cupcake":
        print(order, "Box")
    elif order == "Bread":
        print(order, "Bag")
    elif order == "Meat Pie":
        print(order, "Wrap")
    else:
        print("Pack in a paper bag")