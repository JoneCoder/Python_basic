#Comments
#Variables
#Operators

#single line comment

"""multiline
comment"""

#variables

name = "Grocery List"
detail = "Buy from supershop"
number_of_items = 5
budget = 2500 #taka
amount_of_rice = 1.56 #kg
should_we_buy_today = True

print(name, type(name))
print(detail, type(detail))
print(number_of_items, type(number_of_items))
print(budget, type(budget))
print(amount_of_rice, type(amount_of_rice))
print(should_we_buy_today, type(should_we_buy_today))    

#python Reserved Words:
"""False    class    finally    is        return
   None     continue for        lambda    try
   True     def      from       nonlocal  while
   and      del      global     not       with
   as       elif     if         or        yield
   assert   else     import     pass      
   break    except   in         raise"""

#camel case
firstName = "Shariful"

#snake case
last_name = "Islam"

#python duck type language
age = 5
print(age)

age = 5.5
print(age)

age = "string"
print(age)
#static type language
#age:int = 23

#Pytho Operators

number_of_items = 5
print(number_of_items)

number_of_items = number_of_items + 2
print(number_of_items)

number_of_items += 2
print(number_of_items)


x = 10
y = 2
result = x / y
print(result)

#type custing
x = 15
y = 2
result = int(x / y)
print(result)

#Python Arithmatic Operators
#Binary operators
"""+    -    *
	  /    %"""
#Unary operator
"""++    __    **
	 //"""


#Oparetion of arithmatic operators

#Addition:
number_1 = 23
number_2 = 43
result = number_1 + number_2
print("Addition is two value:",result)


#subtraction
number_1 = 24
number_2 = 20
result = number_1 - number_2
print("Subtraction is two value:",result)


#Division
number_1 = 224
number_2 = 12
result = number_1 / number_2
print("Division is two value:",result)


#multiplication
number_1 = 45
number_2 = 6
result = number_1 * number_2
print("Multiplication is two value:",result)


#modulus
number_1 = 125
number_2 = 35
result = number_1 % number_2
print("Modulus is two value:",result)


#Positive to Negative
x = 12
x = -x

print(x)
print(abs(x))


#Divmod operator
x = 10
y = 3
result = divmod(x,y)
print(result)


#Exponential operator
x = 2
result = x ** 4
print(result)

x = 3
result = pow(x, 4)
print(result)


#Assignment operators
"""=    +=    -=
	 /=    %=    *="""

#Conditional operators
"""<    <    <=
	 >=    ==    !=
	 	===   !=="""

#Logical operators
"""and    or
    not"""