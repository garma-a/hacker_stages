counter = 0
while counter < 3:
    user_password = input("Enter your password: ")
    if user_password == "s3cr3t":
        print("Access allowed!")
        break
    else:
        counter += 1
        print("Access Denied!")

print("you tried 3 times the system now is locked !")
