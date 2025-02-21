import numpy as np

rules = []
pages = []
new_pages = []
the_sum = 0

with open("5.txt", "r") as file:
    file = file.readlines()
    for line in file:
        stripped_line = line.rstrip()
        
        if not stripped_line:
            continue
        elif "|" in stripped_line:
            rules.append(stripped_line)
        else:
            pages.append(stripped_line)

rules_without_delimiter = np.loadtxt(rules, delimiter="|")
rwd_to_list = np.ndarray.tolist(rules_without_delimiter)

# sort rules by first number in descending order because why not
for length in range(len(rwd_to_list)):  
    for i in range(len(rwd_to_list)):
        if i == len(rwd_to_list) - 1:
            break
        if rwd_to_list[i][0] < rwd_to_list[i+1][0]:
            rwd_to_list[i], rwd_to_list[i+1] = rwd_to_list[i+1], rwd_to_list[i]     

for line in pages:
    new_line = line.split(",")
    new_pages.append(new_line)

int_list = [[int(num) for num in sublist] for sublist in rwd_to_list] 
new_pages = [[int(num) for num in sublist] for sublist in new_pages]

correctly_ordered = []

for line in new_pages:
    to_swap = False

    for num1, num2 in int_list:
        if num1 in line and num2 in line:
            index1 = line.index(num1)
            index2 = line.index(num2)

            if index1 > index2:
                to_swap = True
                break

    if not to_swap:
        correctly_ordered.append(line)

to_sum = []

for line in correctly_ordered:
    line_length = len(line)

    if line_length % 2 == 0:
        continue
    else:
        to_sum.append(line[line_length // 2])

for i in to_sum:
    the_sum += i
    
print(the_sum)