numb_names = int(input("Enter number of names: "))
even_set = set()
odd_set = set()



for i in range(numb_names):
    name = input("Enter name:")
    sum_of_ascii = 0
    for char in name :
        sum_of_ascii += ord(char)
    sum_of_ascii = sum_of_ascii // (i + 1)
    if sum_of_ascii % 2 == 0:
        even_set.add(sum_of_ascii)
    if sum_of_ascii % 2 != 0:
        odd_set.add(sum_of_ascii)

if sum(even_set) >= sum(odd_set):
    print(", ".join([str(x) for x in even_set.difference(odd_set)]))
if sum(odd_set) > sum(even_set):
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))
    
if(sum(even_set) == sum(odd_set)):
    print(", ".join([str(x) for x in even_set.union(odd_set)]))