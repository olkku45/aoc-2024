lines = []
safe_rows = 0

with open("2.txt", "r") as file:
    for line in file:
        lines.append(line.split())

for row in lines:
    numbers = [int(number) for number in row]

    asc = all(num1 <= num2 for num1, num2 in zip(numbers, numbers[1:]))
    desc = all(num1 >= num2 for num1, num2 in zip(numbers, numbers[1:]))
    max_differ = all(abs(num1 - num2) <= 3 for num1, num2 in zip(numbers, numbers[1:]))
    equal_numbers = any(num1 == num2 for num1, num2 in zip(numbers, numbers[1:]))

    if (asc or desc) and max_differ and not equal_numbers:
        safe_rows += 1

print(safe_rows)