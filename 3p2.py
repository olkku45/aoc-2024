'''pitää löytää do ja don't ilmaisut tiedostosta, ja 
lukea tiedostosta niiden mukaan. don't-ilmaisun jälkeen
tulevia mul-statementtejä ei lasketa, ja do-ilmaisun
jälkeen tulevat lasketaan'''

import re

def extract_mul_statements(text):
    pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
    is_enabled = True  # Start with reading enabled
    matches = []

    # Tokenize by splitting non-alphanumeric characters (except '-')
    tokens = re.split(r'[^a-zA-Z0-9-]+', text)

    for token in tokens:
        if "don't" in token:  
            is_enabled = False  # Disable reading
        elif "do" in token:  
            is_enabled = True  # Enable reading

        if is_enabled:
            found = re.findall(pattern, token)
            matches.extend([(int(x), int(y)) for x, y in found])

    return matches

# Sample text (one line)
text = "mul(2,4)&mul(3,7)!^don't()_mul(5,5)+mul(32,64)(mul(11,8)undo()?mul(8,5))"

# Run function
result = extract_mul_statements(text)
print(result)

# TEHTY CHATGPT:LLÄ TEE JOSKUS OMA