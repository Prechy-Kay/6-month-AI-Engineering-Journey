age = 18
is_registered = True
has_ticket = True

if age >= 18 and not is_registered:
    print("Please register first.")
elif age >= 18 and not has_ticket and is_registered:
    print("Ticket required.")
elif age >= 18 and has_ticket and is_registered:
    print("Check-in successful.")
else:
    print("You must be 18 or older to check in.")