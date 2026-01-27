names = int(input("Enter the number of usernames: "))
unique_usernames = set()
for i in range(names):
    unique_usernames.add(input("Enter username: "))

print(" ".join(unique_usernames))