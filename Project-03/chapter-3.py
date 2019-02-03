# author Md. Shariful

# condition

num = 50
# num = input("Please input a number: ")
num = int(num)
if num % 2 == 0:
	print("Even Number")
	print("Thank You!")
else:
	print("Odd Number")
	print("Thank You!")

num2 = 100
# num2 = input("Please input a number: ")
num2 = int(num2)
if num2 == 50:
	print("Half Century")
elif num2 == 100:
	print("Century")
elif num2 > 100:
	print("Century+")
else:
	print("unknown number!")


# Logical operator and or
num = 3
if num >= 3 and num < 5:
	print("3 to 5")

num = 5
if num >= 3 or num < 5:
	print("5 or -4")

# compare string
name1 = "Shariful"
name2 = "shariful"

if name1 == name2:
	print("Same Name")
else:
	print("Name doesn't match")

# Not equals to
name = "unknown person"
if name != "Shariful":
	print(name)

# while loop
'''
while condition:
	body
'''
x = 0
while x <= 10:
	print(x)
	x += 1

# infinite loop
n = 1
while True:
	print(n)
	n += 1
	if n > 20:
		break

# Omit even number 1 to 20
x = 0
while x <= 20:
	x += 1
	if x % 2 == 0:
		continue
	print(x)

# for loop
'''
for elemnet in iterable:
	body
'''
sum = 0
for num in range(1, 11):
	print(num)
	sum += num
print ("Sum is {sum}".format(sum = sum))

title = "Apple Inc"
for char in title:
	print(char)