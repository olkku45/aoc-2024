left = []
right = []
total_distance = 0

with open("1.txt", "r") as file:
    for line in file:
        lines = line.split()
        left.append(int(lines[0]))
        right.append(int(lines[1]))

while left and right:
    min_left = min(left)
    min_right = min(right)
    left.remove(min_left)
    right.remove(min_right)

    distance = max(min_left, min_right) - min(min_left, min_right)
    total_distance += distance

print(total_distance)