left = []
right = []
total_similarity_score = 0

with open("1.txt", "r") as file:
    for line in file:
        lines = line.split()
        left.append(int(lines[0]))
        right.append(int(lines[1]))

for left_number in left:
    for right_number in right:
        if left_number == right_number:
            total_similarity_score += left_number

print(total_similarity_score)