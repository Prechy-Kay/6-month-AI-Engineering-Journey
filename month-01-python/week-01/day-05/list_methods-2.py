orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
removed_order = orders.pop(1)
print(removed_order)
print(orders)


orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
orders.pop()    # It's without an idex. It removes the last item in the list.
print(orders)


orders = ["Meat Pie", "Cake", "Bread", "Cupcake"]
orders.sort()
print(orders)


orders = ["Cake", "Bread", "Cupcake", "Meat Pie"]
orders.sort(reverse=True)
print(orders)


orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
orders.reverse()
print(orders)


# append()   - Add to the end
# remove()   - Remove by value
# insert()   - Add at a specific index
# pop(1)     - Remove by index
# pop()      - Remove by last item
# sort()     - Sort the list according to their natual order
# reverse()  - Reverse the current order
# sort(reverse=True) - Arranges the list in descending alphabetical order, from Z → A.