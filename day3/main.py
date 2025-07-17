from variables.userInput import userInput
from variables.userInput import printList

def shoppingList():
    shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
    print(shopping_list)
    print(type(shopping_list))
    print(shopping_list[0])
    print(shopping_list[4])
    shopping_list[1] = "rice"
    print(shopping_list[1])
    shopping_list.append("carrots")
    if (len(shopping_list) == 6):
        print("shopping_list has 6 elements")

    shopping_list.extend(["toffee", "coffee"])
    print(shopping_list)
    shopping_list.pop(2)
    print(shopping_list)
    shopping_list.pop()
    print(shopping_list)

def userDeets():
    user_details_list = userInput() # returns list with 4 elements: name, age, dob, height
    print(user_details_list[0:3])
    if(type(user_details_list[1]) == int):
        print("age is an int")
    print(f"height: {user_details_list[3]}")

def mixTask():
    mixture = [1, 2, 3, "one", "two", "three"]
    print(mixture)

    print(mixture[1:3])
    print(mixture[0:len(mixture)-1:2])
    print(mixture[-1:-3:-1])


def game():
    # "Stranded on a Desert Island" game
    # Rationale: Practice tuples
    # Type of exercise: Finish the code
    print("You are stranded on a desert island. You can take only THREE items.")
    essential_item1 = input("What is an essential item you would take? ")
    essential_item2 = input("What is an essential item you would take? ")
    essential_item3 = input("What is an essential item you would take? ")
    # save the items as a tuple
    essentials_tuple = (essential_item1, essential_item2, essential_item3)  # YOUR CODE GOES HERE INSTEAD OF 'None'
    # print the tuple
    print("Here are your items as a tuple:", essentials_tuple)
    print("")
    print("I lied. You can take one more item.")
    essential_item4 = input("What is one more essential item you would take? ")
    # try to add the 4th item to the tuple
    # if you can't add the 4th item, work out how to save the 4th item to the tuple
    # YOUR CODE GOES HERE
    essential_item4 = (essential_item4,)
    essentials_tuple += essential_item4
    print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)


def dictTask():
    student_1 = {
        "name": "susan",
        "stream": "tech",
        "completed_lessons": 4,
        "completed_lesson_names": ["variables", "data_types", "set up"]
    }
    # Explain how a dictionary saves/structures data? Example, what does each value need to be accompanied/associated with?

    print(student_1)
    print(type(student_1))
    streamVal = student_1["stream"]
    print(streamVal)
    clnVal = student_1["completed_lesson_names"]
    print(clnVal)
    print(type(clnVal))
    print(clnVal[0])
    student_1["completed_lessons"] = 3
    print(student_1)
    student_1["completed_lesson_names"].pop(1)
    #print(student_1)
    print(student_1.keys())

# Outcome (By doing this you should): Practice using lists and dictionaries

# Script should act like a waiter at a restaurant taking orders


# level 1

def orderTask():
    # Greet the user
    print("Hello, welcome to our fine establishment, my name is Greg and I will be taking your order today.")

    # Print a list of starters
    startersList = ["Salad", "Bread", "calamari"]
    printList(startersList, "starters")

    # Take an input for the user for their starter
    userStartIn = input("please enter the corresponding number to your starter choice: ")

    # Print a list of mains
    mainsList = ["Roast chicken", "T-Bone steak", "Crispy Duck", "Burger", "Pizza"]
    printList(mainsList, "mains")


    # Take an input for the user for their main course
    userMainIn = input("please enter the corresponding number to your starter choice: ")

    # Print a list of desserts
    desertList = ["Ice cream", "Apple pie", "Cake"]
    printList(desertList, "deserts")

    # Take an input for the user for their dessert
    userDesertIn = input("please enter the corresponding number to your starter choice: ")

    # Print all of the user's choices
    print("ah, " + userStartIn + ", ", userMainIn + ", ", userDesertIn + " . Great choices!" )

    # level 2

    # Use at least one f-string

    # Add each item ordered to a list called 'customer_order_list'


    # level 3 (may need research if we have not covered dictionaries yet)

    # Use dictionaries and assign prices to the items. Create a bill at the end of the program.


    # level 4

    # Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.

while True:
    print("Main menu - select the task with the correct number")
    print("1 - shopping list task")
    print("2 - game task")
    print("3 - dict task")
    print("4 - mixture task")
    print("5 - userDetail task")
    print("6 - exit")

    choice = input("Enter a number (1–6): ")


    match choice: # switch staments
        case "1":
            shoppingList()
        case "2":
            game()
        case "3":
            dictTask()
        case "4":
            mixTask()
        case "5":
            userDeets()
        case "6":
            print("exiting" )
            break
        case _:
            print("Invalid choice. Please select 1–6.")
