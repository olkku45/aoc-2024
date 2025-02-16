pattern = "XMAS"
lines = []

with open("4.txt", "r") as file:
    for line in file:
        stripped_line = line.rstrip()
        lines.append(stripped_line)


class WordSearch:
    
    
    def horizontal_search(file):
        xmas_counter = 0

        for line in lines:
            if pattern in line:
                xmas_counter += 1

        return xmas_counter


    def vertical_search(file):
        xmas_counter = 0

        max_length = max(len(line) for line in lines)
        vertical_lines = [[] for _ in range(max_length)]
        
        for line in lines:
            line.strip()
            for i in range(max_length):
                if i < len(line):
                    vertical_lines[i].append(line[i])
                else:
                    vertical_lines[i].append(" ")
        
        columns = ["".join(column) for column in vertical_lines]

        for column in columns:
            if pattern in column:
                xmas_counter += 1

        return xmas_counter


    def diagonal_search(file):
        pass


    def backwards_search(file):
        xmas_counter = 0

        for line in lines:
            line = line[::-1]
            if pattern in line:
                xmas_counter += 1
        
        return xmas_counter


    def overlapping_search(file):
        pass


total_xmas_counter = WordSearch.vertical_search(file)
