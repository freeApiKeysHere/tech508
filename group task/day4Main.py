def print_something():
    print("something")

def print_something_v2(x):
    print(x)

def greet(x):
    print(f"Hello, my name is {x}")

def addition(int1, int2):
    return int1 + int2

def addition2(int1 = 2, int2 = 2):
    return int1 + int2

def print_every_number(*nums): # * char allows for multi args
    print(type(nums))
    for x in nums:
        print(x)
#print_every_number(1,2,3,4,5,6,6,6,6)

def greetV2(x: str):
    print(f"Hello, my name is {x}")
#greetV2(111)

def division(x: int = 2, y: int = 5) -> float:
    return x/y
a = 4
b = 6
print(division())