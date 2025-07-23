x = 0 # commenting this out leads to a not defined error

while x < 10:
    print(x)
    x += 1 # no ++ operator? ; without this there is an infinite loop

print()

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1