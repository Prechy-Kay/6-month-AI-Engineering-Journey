orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
prices = [5000, 1500, 2000, 2500]
for number in range(4):
    print(number + 1, ".", orders[number], "-", "₦", prices[number])



orders = ["Cake", "Cupcake", "Bread", "Meat Pie"]
prices = [5000, 1500, 2000, 2500]
quantities = [2, 6, 3, 4]
for number in range(4):
    print(number + 1, ".", orders[number], "-", "₦", prices[number], "*", quantities[number], "=", prices[number] * quantities[number])

    