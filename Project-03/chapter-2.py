#author Md. Shariful Islam

#Statment
print("Hello world!")
x = 2

#Expression
#variable operator value === Expression

y = x + 2

#String
title = 'Python course'
print(title[0], title[1], title[2], title[-1], title[-2])

#String is a imutable object inpython

#String operation
name = 'jonathon swift'
print(name.title())
print(name.upper())
print(name.lower())

#string concatenation
first_name = 'Steve'
last_name = 'Jobs'

name = first_name + ' ' + last_name
print(name)

name = first_name + '\n' + last_name	# '\n' is special charter
print(name)

#String whitespace
name = "   Mr. X   "
print("_"+ name +"_")
print("_"+ name.lstrip() +"_")
print("_"+ name.rstrip() +"_")
print("_"+ name.strip() +"_")

#Printing Single and Double Quote
shop_name = "Rahim's Shop"
print(shop_name)

shop_name = 'Rahim"s Shop'
print(shop_name)

shop_name = 'Rahim\'s Shop'
print(shop_name)

#Find Word in sentence
sentence = "A quick brown fox jumps over the lazy dog"
print(sentence.find('fox'))
print(sentence.find('foxs'))	# -1 the value not found

#Replace text
sentence = "A quick brown fox jumps over the lazy dog"
sentence = sentence.replace('fox', 'tiger')
print(sentence)

sentence = "A quick brown fox jumps over the lazy fox"
sentence = sentence.replace('fox', 'tiger')
print(sentence)

#print Separator
x = "Dhaka"
y = "Bogra"
z = "Comilla"

# Dhaka | Bogra | Comilla

print(x + " | " + y + " | " + z)
#print( x, y, z, sep="|")

#String Interpolation
person = "MR. X's age is 77"
print(person)

person = "{name}'s age is {age}"
print(person.format(name ='Hasib', age = 55))

person = "%s\'s age is %d"
print(person % ("Bill", 44))

#String Slice
name = "Taylor Swift"
part_of_name = name[0:6]
print(part_of_name)