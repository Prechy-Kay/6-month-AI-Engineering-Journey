orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
orders.append("Cookies") # add an item
print(orders)


orders.remove("Bread") # remove an item by value not index
print(orders)


orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
orders.insert(1, "Cookies")  # add an item at a specific index position shifting everything after it to the right.
print(orders)



orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
orders.pop(2)     # removes by index
print(orders)