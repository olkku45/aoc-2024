pattern = ["MAS", "SAM"]
lines = []

with open("4.txt", "r") as file:
    for line in file:
        stripped_line = line.rstrip()
        lines.append(stripped_line)

xmas_counter = 0
found_positions = set()

rows = len(lines)
cols = len(lines[0])

for x in range(rows - 2):
    for y in range(cols - 2):
        chunk = [line[y:y+3] for line in lines[x:x+3]]

        if len(chunk) == 3 and all(len(row) == 3 for row in chunk):

            first_diag = "".join([chunk[0][0], chunk[1][1], chunk[2][2]])
            second_diag = "".join([chunk[0][2], chunk[1][1], chunk[2][0]])

            if first_diag in pattern or second_diag in pattern:
                if (x,y) not in found_positions:
                    xmas_counter += 1
                    found_positions.add((x,y))
                    