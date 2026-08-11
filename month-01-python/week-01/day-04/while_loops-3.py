number = 0

while number < 10:
    number = number + 1
    if number % 2 == 0:
        name = "even"
    else:
        name = "odd"
    print(number, "is", name)