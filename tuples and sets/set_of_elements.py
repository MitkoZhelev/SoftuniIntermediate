set_len1, set_len2 = input().split()
set1 = set()
set2 = set()
set_len1 = int(set_len1)
set_len2 = int(set_len2)

for i in range(set_len1):
    element = input()
    set1.add(element)
for j in range(set_len2):
    element = input()
    set2.add(element)

present_elements = set1.intersection(set2)

for element in present_elements:
    print(element)