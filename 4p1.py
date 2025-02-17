import re

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
            matches = re.finditer(pattern, line)
            for _ in matches:
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
            matches = re.finditer(pattern, column)
            for _ in matches:
                xmas_counter += 1

        return xmas_counter


    def diagonal_search(file):
        xmas_counter = 0
        
        with open("3.txt", "r") as file:
            file = file.read()

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
        reversed_columns = [i[::-1] for i in columns]
        second_list = []
        third_list = []  # this naming doesn't make sense I know
        a = len(reversed_columns)
        b = len(reversed_columns[0])

        for i in range(b):
            new_tuple = tuple(reversed_columns[j][i-j] for j in range(min(i + 1, a)))
            second_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        for i in range(1, b):
            new_tuple = tuple(reversed_columns[j][b - (j-i) - 1] for j in range(i, a))
            second_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        for i in range(b):
            new_tuple = tuple(columns[j][i-j] for j in range(min(i + 1, a)))
            third_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        for i in range(1, b):
            new_tuple = tuple(columns[j][b - (j-i) - 1] for j in range(i, a))
            third_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        
        for item in second_list:
            item = "".join(item)
            matches = re.finditer(pattern, item)
            for _ in matches:
                xmas_counter += 1
            
        for item in third_list:
            item = "".join(item)
            matches = re.finditer(pattern, item)
            for _ in matches:
                xmas_counter += 1

        return xmas_counter


    def backwards_search(file):
        xmas_counter = 0

        # backwards horizontal
        for line in lines:
            line = line[::-1]
            matches = re.finditer(pattern, line)
            for _ in matches:
                xmas_counter += 1

        # backwards vertical
        max_length = max(len(line) for line in lines)
        vertical_lines = [[] for _ in range(max_length)]
        
        for line in lines:
            line.strip()

            for i in range(max_length):
                if i < len(line):
                    vertical_lines[i].append(line[i])
                else:
                    vertical_lines[i].append(" ")
        
        reversed_vert_lines = [i[::-1] for i in vertical_lines]
        columns = ["".join(column) for column in reversed_vert_lines]

        for column in columns:
            matches = re.finditer(pattern, column)
            for _ in matches:
                xmas_counter += 1

        #backwards diagonal
        with open("3.txt", "r") as file:
            file = file.read()

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
        reversed_columns = [i[::-1] for i in columns]
        second_list = []
        third_list = []
        a = len(reversed_columns)
        b = len(reversed_columns[0])

        for i in range(b):
            new_tuple = tuple(reversed_columns[j][i-j] for j in range(min(i + 1, a)))
            second_list.append(new_tuple[0] if len (new_tuple) == 1 else new_tuple)

        for i in range(1, b):
            new_tuple = tuple(reversed_columns[j][b - (j - i) - 1] for j in range(i, a))
            second_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        for i in range(b):
            new_tuple = tuple(columns[j][i-j] for j in range(min(i + 1, a)))
            third_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        for i in range(1, b):
            new_tuple = tuple(columns[j][b - (j-i) - 1] for j in range(i, a))
            third_list.append(new_tuple[0] if len(new_tuple) == 1 else new_tuple)

        reversed_diag_lines_second = [i[::-1] for i in second_list]
        reversed_diag_lines_third = [i[::-1] for i in third_list]

        for item in reversed_diag_lines_second:
            item = "".join(item)
            matches = re.finditer(pattern, item)
            for _ in matches:
                xmas_counter += 1

        for item in reversed_diag_lines_third:
            item = "".join(item)
            matches = re.finditer(pattern, item)
            for _ in matches:
                xmas_counter += 1
        
        return xmas_counter
    

total_xmas_counter = WordSearch.vertical_search(file)+WordSearch.backwards_search(file)+WordSearch.diagonal_search(file)+WordSearch.horizontal_search(file)
print(total_xmas_counter)