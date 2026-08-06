registered = True
has_ticket = False

if registered:
    if has_ticket:
        print("Check-in successful.")
    else:
        print("Ticket required.")
else:
    print("Please register first.")
# This will print -- Ticket required.



registered = False
has_ticket = True

if registered:
    if has_ticket:
        print("Check-in successful.")
    else:
        print("Ticket required.")
else:
    print("Please register first.")
# This will print -- Please register first.