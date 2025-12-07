users = {
    "alice": "password123",
    "bob": "qwerty456",
    "mohamed": "secret789"
}

username = input("Enter username: ")
password = users.get(username)

if password:
    print(f"Password for {username}: {password}")
else:
    print("Username not found.")
