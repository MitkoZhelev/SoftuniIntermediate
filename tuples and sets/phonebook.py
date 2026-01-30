contacts = {}

while True:
    entry = input("Enter a contact name and number:")
    if entry.isnumeric():
        break
    name, number = entry.split('-')
    contacts[name] = number

for i in range(int(entry)):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")