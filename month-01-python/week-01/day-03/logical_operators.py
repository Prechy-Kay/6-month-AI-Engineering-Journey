age = 22
is_student = True
has_id = False

if age < 18:
    print("Too young.")
elif is_student and has_id:
    print("Student access granted.")
elif is_student and not has_id:
    print("Student ID required.")
else:
    print("Access denied.")

# NOTE: The condition that runs is the one that's True. So if it's not true, it won't run.
