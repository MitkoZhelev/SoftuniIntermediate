numb_of_numbers = int(input("Enter number of sets: "))
max_distance = 0
points = []
for _ in range(numb_of_numbers):
    firstSet, secondSet = input().split("-")

    start1, end1 = map(int, firstSet.split(","))
    start2, end2 = map(int, secondSet.split(","))


    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    distance = intersection_end - intersection_start + 1
    if distance > max_distance:
        max_distance = distance
        points = [x for x in range(intersection_start, intersection_end + 1)]

print(f"Longest intersection is {points} with length {max_distance}")