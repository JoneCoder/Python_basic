sing = input('Type your Operation first letter: ')
if sing == 's':
    squerNumber = float(input('Enter a number: '))
    import math
    result = math.sqrt(squerNumber)
    print (result) 
else:
    firstNumber = float(input('Enter a number: '))
    secondNumber = float(input('Enter an another number: '))
    def basicCalculator():
        if sing == 'a':
            add = firstNumber + secondNumber
            print (add)
        elif sing == 'b':
            subtracting = firstNumber - secondNumber
            print(subtracting)
        elif sing == 'm':
            multiple = firstNumber * secondNumber
            print(multiple)
        elif sing == 'd':
            divided = firstNumber / secondNumber
            print(divided)
        elif sing == 'r':
            remainder = firstNumber % secondNumber
            print (remainder)
    display = basicCalculator()