import random
step = int(input("Do you want Easy mode press 1 or Medium mode press 2 or Hard mode press 3__"))

if step == 1:
    number = random.randint(1, 50)
    attempts = 0
    
    while True:
        input_number = int(input("Guess the number (between 1 and 50): "))
        attempts += 1
        if input_number == number:
            print("YES, your guess is correct!")
            a = input("Exit to type \'E\' or Continue to type \'C\' and press Enter.")
            if a == "E":
                break
            elif a == "C":
                continue
        
        if input_number > number:
            print("Incorrect! Please try to guess a smaller number.")
        else:
            print("Incorrect! Please try to guess a larger number.")

    print("You tried", attempts, "times to find the correct number")


elif step == 2:
    number = random.randint(1, 500)
    attempts = 0
    
    while True:
        input_number = int(input("Guess the number (between 1 and 500): "))
        attempts += 1
        if input_number == number:
            print("YES, your guess is correct!")
            a = input("Exit to type \'E\' or Continue to type \'C\' and press Enter.")
            if a == "E":
                break
            elif a == "C":
                continue
        
        if input_number > number:
            print("Incorrect! Please try to guess a smaller number.")
        else:
            print("Incorrect! Please try to guess a larger number.")

    print("You tried", attempts, "times to find the correct number")


elif step == 3:
    number = random.randint(1, 1000)
    attempts = 0
    
    while True:
        input_number = int(input("Guess the number (between 1 and 1000): "))
        attempts += 1
        if input_number == number:
            print("YES, your guess is correct!")
            a = input("Exit to type \'E\' or Continue to type \'C\' and press Enter.")
            if a == "E":
                break
            elif a == "C":
                continue
        
        if input_number > number:
            print("Incorrect! Please try to guess a smaller number.")
        else:
            print("Incorrect! Please try to guess a larger number.")

    print("You tried", attempts, "times to find the correct number")