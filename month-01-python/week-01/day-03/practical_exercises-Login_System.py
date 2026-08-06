username = "Precious"
password = "python123"

if username == "Precious" and password == "python123":
    print("Login successful.")
elif not username == "Precious" and password == "python123":
    print("Incorrect username.")
elif username == "Precious" and not password == "python123":
    print("Incorrect password.") 
else:
    print("Incorrect username and password.")