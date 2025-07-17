from variables.variables_examples import add, sub, mult, div

while True:
    print("this is a calc \nEnter your option below\n 1 - add\n 2 - sub\n 3 - mult\n 4 - div\n 5 - Exit")
    x = input("Enter your choice: ")
    match x: # switch statements
        case "1":
            a = float(input("Enter first number"))
            b = float(input("Enter second number"))
            print(add(a, b))
        case "2":
            a = float(input("Enter first number"))
            b = float(input("Enter second number"))
            print(sub(a, b))
        case "3":
            a = float(input("Enter first number"))
            b = float(input("Enter second number"))
            print(mult(a, b))
        case "4":
            a = float(input("Enter first number"))
            b = float(input("Enter second number"))
            print(div(a, b))
        case "5":
            print("exiting")
            break
        case _:
            print("Invalid choice. Please select 1–5.")
