result = 0
for num in range(101):
    if num % 5 == 0:
        print(num)
        result += num
print("sum is:", result)

result2 = 0
for num in range(5, 101,5):
    print (num)
    result2 += num
print("sum is:", result2)