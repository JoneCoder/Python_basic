def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print ("You can't divide by zero")
    except TypeError:
        print ("Data type not supported")
    except ValueError:
        print("String are not supported")
    else:
        return result;
    finally:
        print ("Inside finally")
        
a = float(input())
b = float(input())
print (divide(a,b))

for i in range(10):
    print (i)
else:
    print ("Inside else")

for x in range(20):
    print (x)
    break
else:
    print ("Inside esle")