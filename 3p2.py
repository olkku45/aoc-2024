import re
n = 5
pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
result = 0

with open("3.txt", "r") as file:
    file = file.read()


def reconstruct(groups):
    original = groups[0]
    for i in range(1, len(groups)):
        original += groups[i][-1]
    
    return original


def reading_check(file):
    file_copy = [file[i:i+n] for i in range(len(file))]
    reading = True
    removed = []

    while file_copy:
        part = file_copy.pop(0)
        removed.append(part)

        if "don't" in part:
            reading = False
        elif "do" in part:
            reading = True

        if not reading:
            while file_copy:
                part = file_copy.pop(0)
                
                if "do" in part:
                    reading = True
                    break

    print(removed)
    reconstructed = reconstruct(removed)
    return reconstructed    


file = reading_check(file)
number_pairs = re.findall(pattern, file)

for pair in number_pairs: 
    pair = list(pair)
    multiplied = int(pair[0]) * int(pair[1])
    result += multiplied

print(result)