age = 18
has_ticket = True
is_member = True

if age >= 18 and has_ticket and is_member:
    print("You can enter.")
elif age >= 18 and not has_ticket:
    print("Ticket required.")
elif age >= 18 and has_ticket and not is_member:
    print("Membership required.")
else:
    print("You are too young.")