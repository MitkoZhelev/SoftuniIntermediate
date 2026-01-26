quantity_of_food = int(input("Enter the number of food items: "))

food_stack = list(map(int, input("Enter the food items separated by space: ").split()))
max_food = max(food_stack)
while food_stack:
    food = food_stack[0] # look at the first order

    if quantity_of_food - food >= 0:
        quantity_of_food -= food
        food_stack.pop(0)      # remove fulfilled order
    else:
        print(quantity_of_food)
        print("Orders left: " + " ".join(food_stack))
        break
else:
    print("Orders complete")