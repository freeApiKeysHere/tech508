#instructions not clear
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

print(dict_data[1]["name"])
print("1. Loop through a list")
for x in range(len(list_data)):
    print(f"num {x+1}: {2*list_data[x]}")
print()

print("2. Loop through the 'embedded_lists' list ")
for x in range(len(embedded_lists)):
    print(embedded_lists[x])
print()

print("3. Loop through the lists embedded inside a list ")
for x in range(len(embedded_lists)):
    print(embedded_lists[x])
    for y in range(len(embedded_lists[x])):
        print(embedded_lists[x][y])
print()

print("4. Loop through a dictionary ")
for x in dict_data.keys():
    print(x)
print()

print("5. Loop through a dictionary and print its values ")
for x in dict_data.values():
    print(x)
print()

print("6. Loop to print the values of the dictionary items inside a dictionary ")
for x in dict_data.values():
    for y in x.values():
        print(y)
print()

print("7. Loop to print specific values of the dictionary items inside a dictionary ")
for x in dict_data.values():
    print(x["money"])
print()

print("8. Loop through a list with a nested if statement ")
for x in range(len(list_data)):
    if list_data[x] < 3:
        print("less than 3")
    if list_data[x] == 3:
        print("I found three")
    if list_data[x] > 3:
        print("greater than 3")
#sdaf