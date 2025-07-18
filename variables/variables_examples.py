a = int(5)
b = float(5.55)
c = str("dog")
# '==' is a comparison operator that is used to check if 2 values are equal eg '5 == a' is true

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

def mod(x,y):
    return x%y

def gr8Than():
    print("comparing 3 and 2 with '3 > 2'")
    if(3>2):
        print("3 is greater than 2")


def lessThan():
    print("comparing 3 and 2 with '2 < 3'")
    if(2<3):
        print("2 is less than 3")


def isEqual():
    print("comparing 2 and 2 with '=='")
    if (2==2):
        print("2 is equal to 2")


def notEqual():
    print("comparing 2 and 4 with '!='")
    if (2!=4):
        print("2 is not equal to 4")

def lessThanPlus():
    print("comparing 7 with 7 and 8 with '<='")
    if (7<=7 & 7<=8):
        print("7 is less than or equal to 7 and 7 is less than or equal to 8")


def gr8ThanPlus():
    print("comparing 10 with 10 and 9 with '>='")
    if (10>=10 & 10>=11):
        print("10 is greater than or equal to 10 and 10 is greater than or equal to 9")

#print(5==5)