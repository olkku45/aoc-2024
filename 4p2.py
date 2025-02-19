lines = []

with open("4.txt", "r") as file:
    for line in file:
        stripped_line = line.rstrip()
        lines.append(stripped_line)

rows = len(lines)
cols = len(lines[0])
xmas_counter = 0

for x in range(rows):
    for y in range(cols):
        chunk = [line[y:y+3] for line in lines[x:x+3]]

        if len(chunk) == 3 and all(len(row) == 3 for row in chunk):
            if chunk[1][1] == "A": 
                concatenated = chunk[0][0] + chunk[0][2] + chunk[2][0] + chunk[2][2]
                joined = "".join(concatenated)
                if joined == "MSMS":
                    xmas_counter += 1
                elif joined == "SMSM":
                    xmas_counter += 1
                elif joined == "MMSS":
                    xmas_counter += 1
                elif joined == "SSMM":
                    xmas_counter += 1

print(xmas_counter)