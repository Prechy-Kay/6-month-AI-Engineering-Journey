for order in range(1, 11):
    if order < 4:  #OR if order <= 3:
        name = "Small"
    elif order < 7:    #OR if order <= 6:
        name = "Medium"
    else:
        name = "Large"
    print("Order", order, name)
    