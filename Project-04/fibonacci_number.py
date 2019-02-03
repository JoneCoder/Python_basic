def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1
    
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next

def list_fib(n):
    list_fib = [1,1]
    if n <= 2:
        return list_fib[:n]
    fib_x, fib_next = 1, 1
    i = 3
    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        list_fib.append(fib_next)
    return(list_fib)
    
if __name__ == "__main__":
    for x in range(1,11):
        print(find_fib(x))
    print(list_fib(10))
    
    
    
    