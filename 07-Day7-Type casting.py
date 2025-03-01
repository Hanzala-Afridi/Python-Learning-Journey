#Two Types of Typecasting:
#Explicit Conversion (Explicit type casting in python)
#Implicit Conversion (Implicit type casting in python).

#Explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

#Implicit type casting:
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))



str1 = "7"          
str2 = "3.142"
str3 = "13"
num1 = 29
num2 = 6.67
A = "10"
B = "20"

print(int(str1))
print(float(str2))
print(float(str3))
print(str(num1))
print(str(num2))
print(float(A + B))
