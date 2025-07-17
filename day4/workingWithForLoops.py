#instructions not clear
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

for x in range(len(list_data)):
    print(f"num {x+1}: {2*list_data[x]}")

for x in range(len(embedded_lists)):
    print(embedded_lists[x])
    for y in range(len(embedded_lists[x])):
        print(embedded_lists[x][y])

for x in dict_data.values():
    print(x)

for x in dict_data.values():
    for y in x.values():
        print(y)

for x in dict_data.values():
    print(x["money"])

for x in range(len(list_data)):
    if list_data[x] < 3:
        print("less than 3")
    if list_data[x] == 3:
        print("I found three")
    if list_data[x] > 3:
        print("greater than 3")
