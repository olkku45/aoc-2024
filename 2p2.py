lines = []
safe_rows = 0

with open("2.txt", "r") as file:
    for line in file:
        lines.append([int(number) for number in line.split()])


def is_safe(numbers):
    
    asc = all(num1 <= num2 for num1, num2 in zip(numbers, numbers[1:]))
    desc = all(num1 >= num2 for num1, num2 in zip(numbers, numbers[1:]))
    max_differ = all(abs(num1 - num2) <= 3 for num1, num2 in zip(numbers, numbers[1:]))
    equal_numbers = any(num1 == num2 for num1, num2 in zip(numbers, numbers[1:]))
    not_empty_list = numbers
    single_number = bool(len(numbers) == 1)

    return (asc or desc) and max_differ and not equal_numbers and not_empty_list and not single_number


for row in lines:

    if is_safe(row):
        safe_rows += 1
        continue

    for i in range(len(row)):
        modified_row = row[:i] + row[i+1:] 
        if is_safe(modified_row):
            safe_rows += 1
            break

print(safe_rows)