number_of_sequenced = input("Enter the number of sequenced items: ")
max_value = 0
min_value = 109
end_stack = []
for  i in range(int(number_of_sequenced)):
    case = input().split()
    number_case = int(case[0])
    if number_case == 1:
        number = int(case[1])
    
        end_stack.append(number)
    if number_case == 2:
        end_stack.pop()
    if number_case == 3:
        if end_stack:
            max_value = max(end_stack)
            print(max_value)
    if number_case == 4:
        if end_stack:
            min_value = min(end_stack)
            print(min_value)
    
print(end_stack[::-1])