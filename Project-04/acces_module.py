step = int(input("Fibonacci Number type 1 or Fibonacci List type 2 and press Enter_"))
import fibonacci_number as fib
if step == 1:
    n = int(input("Input Your Range start point: "))
    n1 = int(input("Input Your Range End Point: "))
    for x in range(n, n1):
        print(fib.find_fib(x))

if step == 2:
    y = int(input("Input a Integer: "))
    print(fib.list_fib(y))