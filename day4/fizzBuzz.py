import time
def fizzBuzzFunc(x: int = 3, y: int = 5):
    for i in range(1, 101):
        # print(x)
        printStr = ""
        if i % x == 0:
            printStr = "Fizz"
        if i % y == 0:
            printStr += "Buzz"
        if printStr == "":
            print(i)
        else:
            print(printStr)


fizzBuzzFunc()
