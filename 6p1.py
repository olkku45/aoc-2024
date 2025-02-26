import random
import time
start_time = time.time()

random_number = random.randint(1, 1000)

with open("6.txt", "r") as file:
    matrix = [list(line.strip()) for line in file]

rows = len(matrix)
cols = len(matrix[0])


def rotate_matrix(matrix):
    # thanks to https://stackoverflow.com/a/53251028
    # matrix rotation 90 degrees counter clockwise
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]


flag = False

while not flag:
    flag = False  # flag for checking whether guard has reached the top row

    for x in range(1, rows):  # x -> y, rows -> cols
        for y in range(cols):  # y -> x, cols -> rows

            if matrix[x][y] == "^":

                if matrix[x - 1][y] == "#":
                    matrix = rotate_matrix(matrix)
                    continue

                else:
                    matrix[x][y], matrix[x - 1][y] = matrix[x - 1][y], matrix[x][y]
                    matrix[x][y] = "X"

                # if guard is at the top row
                if "^" in matrix[0]:
                    col_index = matrix[0].index("^")
                    matrix[0][col_index] = "X"

                    if rows > 1 and matrix[1][col_index] == ".":
                        matrix[1][col_index] = "X"

                    flag = True

        # break loop after guard has gotten to the top row
        if flag == True:
            break

position_counter = 0

for line in matrix:
    for character in line:
        if character == "X":
            position_counter += 1

print(position_counter)
print("--- %s seconds ---" % (time.time() - start_time))