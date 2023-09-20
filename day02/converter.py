
num_char = len(input("What is your name? "))

print(type(num_char))

# we can convert the num_char variable to a string by using the str() function
# str() is a string function that converts the input to a string
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")