terminate_program = False
while not terminate_program:
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    
    while True:
        operation = input("Please type add, sub, mul, div, mod or sqr and exit for type quit: ")
        if operation == "quit":
            terminate_program = True
            break;
        if operation not in ['add', 'sub', 'mul', 'div', 'mod', 'sqr']:
            print("Unknown operation!")
            continue
        if operation == "add":
            print("Result is: ", number1 + number2)
            #continue
            break
        if operation == "sub":
            print("Result is: ", number1 - number2)
            #continue
            break
        if operation == "mul":
            print("Result is: ", number1 * number2)
            #continue
            break
        if operation == "div":
            print("Result is: ", number1 / number2)
            #continue
            break
        if operation == "mod":
            print("Result is: ", number1 % number2)
            #continue
            break
        if operation == "sqr":
            number = int(input("Please enter an integer number: "))
            import math
            square = math.sqrt(number)
            print(square)
            #continue
            break