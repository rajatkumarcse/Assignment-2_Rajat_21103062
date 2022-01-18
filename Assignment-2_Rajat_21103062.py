# Question ---> 1

input_string = "Python is a case sensitive language"

# Part (a)
# To find the length of the input string
print(f"The length of this input string is {len(input_string)}")

# Part (b)
# To reverse the order of the string
print(input_string[::-1])

# Part (c)
# To store "a case sensitive" using slice function in a new string
# index of 'a' is 10 and index of 'e' in sensitive is 25
new_string = input_string[10:26]
print(new_string)

# Part (d)
# To replace a "a case sensitive" with "object oriented"
print(input_string.replace("a case sensitive", "object oriented"))

# Part (e)
# To find index of substring "a" in the given input string
print(input_string.index('a'))

# Part (f)
# To remove the white spaces from the input string
print(input_string.replace(" ", ""))


# Question --->  2

# To store name, SID, department name and CGPA into different variables

data = '''Hey, <|ABC|> Here!
My SID is <|2110XXXX|>
I am from <|XYZ|> department and my CGPA is <|CGPA|>
'''
name = input("Enter your name:\n")
SID = input("Enter your SID:\n")
department = input("Enter your department:\n")
CGPA = input("Enter your CGPA:\n")

data = data.replace("<|ABC|>", name)
data = data.replace("<|2110XXXX|>", SID)
data = data.replace("<|XYZ|>", department)
data = data.replace("<|CGPA|>", CGPA)

print(data)


# Question ---> 3

# To calculate the following using bitwise operators

a = 56
b = 10

# To calculate a & b , & is equivalent to AND
print("The value of a & b is " + str(a & b))

# To calculate a | b , | is equivalent to OR
print("The value of a | b is " + str(a | b))

# To calculate a ^ b , ^ is equivalent to XOR
print("The value of a ^ b is " + str(a ^ b))

# To left shift both a and b with 2 bits
a = a << 2
print("The value of a << 2 is " + str(a))
b = b << 2
print("The value of b << 2 is " + str(b))

# To right shift a with 2 bits and b with 4 bits
a = a >> 2
print("The value of a >> 2 is " + str(a))
b = b >> 4
print("The value of b >> 4 is " + str(b))


# Question ---> 4

# To find greatest of three numbers entered by the user

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num1 > num2):
    f1 = num1
else:
    f1 = num2

if (num1 > num3):
    f2 = num1
else:
    f2 = num3

if (f1 > f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")


# Question ---> 5

# To check if the word "name" is present in the string entered by the user

text = input("Enter the text :\n")

if ("name" in text):
    result = True
else:
    result = False

if (result):
    print("Yes! name is present")
else:
    print("No! name is not present")


# Question ---> 6

# To check whether the given input lengths can form a triangle or not
# Here length of first side is denoted by a , second side by b and third side by c

a = int(input("Enter length of first side : "))
b = int(input("Enter length of second side : "))
c = int(input("Enter length of third side : "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Yes! A triangle can be formed")
else:
    print("No! A triangle can't be formed")

