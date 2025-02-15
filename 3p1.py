import re
result = 0

with open("3.txt", "r") as file:
    file = file.read()

allowed = "(),"

# you don't even need this but whatever
def remove_special(string, allowed=""):

    x = f"[^a-zA-Z0-9{re.escape(allowed)}]" # needed ChatGPT for this shit
    return re.sub(x, "", string)


modified_file = remove_special(file, allowed)
pattern = r"mul\((-?\d+),\s*(-?\d+)\)"  # include only mul(x,y) where x,y are integers, needed ChatGPT for this shit too
number_pairs = re.findall(pattern, modified_file)

for pair in number_pairs: 
    pair = list(pair)
    multiplied = int(pair[0]) * int(pair[1])
    result += multiplied

print(result)