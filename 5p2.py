import numpy as np
from collections import defaultdict, deque

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

rule_list = [[int(num) for num in sublist] for sublist in rwd_to_list] 
new_pages = [[int(num) for num in sublist] for sublist in new_pages]


# just prooompt engineered my way into this shit, I can't do this myself :sob: I really suck, huh
def conditional_topological_sort_sublist_by_sublist(lists, conditions):
    def is_sorted(sublist, conditions):
        for x, y in conditions:
            if x in sublist and y in sublist:
                if sublist.index(x) > sublist.index(y):
                    return False
        return True

    def topological_sort_for_sublist(sublist, conditions):
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        
        for x, y in conditions:
            if x in sublist and y in sublist:
                if y not in graph[x]:
                    graph[x].add(y)
                    in_degree[y] += 1
                if x not in in_degree:
                    in_degree[x] = 0
        
        # Kahn's algorithm
        queue = deque([node for node in sublist if in_degree[node] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result

    sorted_sublists = []
    for sublist in lists:
        if not is_sorted(sublist, conditions):
            sorted_sublists.append(topological_sort_for_sublist(sublist, conditions))

    return sorted_sublists


sorted_sublists = conditional_topological_sort_sublist_by_sublist(new_pages, rule_list)

to_sum = []
for line in sorted_sublists:
    line_length = len(line)

    if line_length % 2 == 0:
        continue
    else:
        to_sum.append(line[line_length // 2])

for i in to_sum:
    the_sum += i
    
print(the_sum)