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
    removed_first = []
    removed_second = []

    # DEBUG
    print(f"(1)Removed First: {len(removed_first)}")
    print(f"(1)Removed Second: {len(removed_second)}")
    print(f"(1)Remaining: {len(file_copy)}")

    while reading:
        to_remove = []

        for index, part in enumerate(file_copy):
            removed_first.append(part)
            to_remove.append(index)

            if "don't" in part:
                reading = False
                break

        for i in reversed(to_remove):
            del file_copy[i]
    
        if len(file_copy) <= 1:
            return
        
    # DEBUG
    print("(2)Removed First:", len(removed_first))
    print("(2)Removed Second:", len(removed_second))
    print("(2)Remaining:", len(file_copy))
        
    while not reading:
        to_remove = []

        #print(list(enumerate(file_copy)))
        for index, part in enumerate(file_copy):
            to_remove.append(index)

            if "do" in part:
                reading = True
                removed_second.append(part)
                break

        for i in reversed(to_remove):
            del file_copy[i]
        
        if not file_copy:
            break
    
    # DEBUG
    print("(3)Removed First:", len(removed_first))
    print("(3)Removed Second:", len(removed_second))
    print("(3)Remaining:", len(file_copy))

    while reading and file_copy:
        removed_second.append(file_copy.pop(0))

    # DEBUG
    print("(4)Removed First:", len(removed_first))
    print("(4)Removed Second:", len(removed_second))
    print("(4)Remaining:", len(file_copy))

    reconstructed = reconstruct(removed_first) + reconstruct(removed_second)
    return reconstructed

file = reading_check(file)
number_pairs = re.findall(pattern, file)

# DEBUG
'''print(f"Extracted text: {file}")  
print(f"Matches found: {number_pairs}")
print(f"Reconstructed text: {reading_check(file)}")'''

for pair in number_pairs: 
    pair = list(pair)
    multiplied = int(pair[0]) * int(pair[1])
    result += multiplied

print(result)