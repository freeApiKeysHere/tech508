def userInput():
    name = str(input("enter name: "))
    age = int(input("enter age: "))
    dob = str(input("enter DOB: "))
    height = float(input("enter height in CM: "))
    return [name, age, dob, height]

#print("name: " + name)
#print("age: "+ age)
#print("DOB: " + dob)

def printList(menuItems, menuName):
    print(f"here is a list of our {menuName}")
    for x in range(len(menuItems)):
        print(str(x + 1) + " - " + menuItems[x])

