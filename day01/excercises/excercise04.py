# 🚨 Don't change the code below 👇
a = int(input("a: "))
b = int(input("b: "))
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# why there is a red line under the code below?
# because the variable a is a string and the variable b is a string and we can't add a string to a string
# so we need to convert the variable a to an integer
# we can do that by using the int() function
# int() function takes a string and converts it to an integer

# 1. create a variable called c and assign it the value of a so that we don't lose the value of a when we assign the value of b to a

a, b = b, a



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: ", a)
print("b: ", b)



# The explanation of the solution:
# ---------------------------------
# we directly swap the values of a and b using tuple unpacking, which is a more Pythonic and concise way to exchange variable values.
# Tuple unpacking, also known as multiple assignment or tuple assignment, is a feature in Python that allows you to assign the elements of a tuple or any iterable (e.g., a list) to multiple variables in a single line of code. This is often used for swapping values between variables, as demonstrated in your initial code and the example I provided.

# Here's a simple example of tuple unpacking:
# Creating a tuple
t = (1, 2)

# Unpacking the tuple into two variables, a and b
a, b = t

print("a:", a)  # Output: a: 1
print("b:", b)  # Output: b: 2

# In the example above, we have a tuple t with two elements (1 and 2), and we use tuple unpacking to assign those elements to the variables a and b. As a result, a gets the value 1, and b gets the value 2.

