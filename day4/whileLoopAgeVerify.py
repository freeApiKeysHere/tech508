user_prompt = True# SET VARIABLE user_prompt TO TRUE

while user_prompt:# PUT BEGINNING OF WHILE LOOP HERE - SHOULD LOOP WHILE user_prompt IS TRUE
    age = input("What is your age? ")
    if age.isdigit() and int(age) <= 117: # PUT IF STATEMENT HERE TO CHECK IF age IS ALL DIGITS
        user_prompt = False # SET user_prompt TO FALSE
    else: # ADD ELSE STATEMENT HERE
        print(f"Your input is not valid, valid inputs consist of: only digits, age under 118")# TELL USER THE PROBLEM WITH THEIR INPUT

print(f"Your age is {age}")
