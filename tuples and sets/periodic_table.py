count = int(input("Enter the number of elements: "))
element_set = set()
for i in range(count):
    elements = input().split()
    element_set.update(elements)

print("\n".join(element_set))