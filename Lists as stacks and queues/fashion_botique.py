clothes_box = list(map(int, input("Enter the clothes items separated by space: ").split()))
capacity_of_rack = int(input("Enter the capacity of the rack: "))
sumOfClothes = 0
racks_used = 1

while clothes_box:
    cloth = clothes_box.pop()  # take the last piece of clothing

    if sumOfClothes + cloth <= capacity_of_rack:
        sumOfClothes += cloth
    else:
        racks_used += 1
        sumOfClothes = cloth  # start a new rack with the current piece of clothing

print(racks_used)