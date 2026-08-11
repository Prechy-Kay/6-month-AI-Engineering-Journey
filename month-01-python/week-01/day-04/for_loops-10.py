for order in range(1, 21):
    if order % 3 == 0 and order % 5 == 0:
        print("FizzBuzz")
    elif order % 3 == 0:
        print("Fizz")
    elif order % 5 == 0:
        print("Buzz")
    else:
        print(order)
