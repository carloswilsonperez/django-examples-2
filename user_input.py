


name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

num = int(input("Enter an integer"))
print("hello" * num)

# If the user inputs 2 * 3, this outputs 6.
result = eval(input("Enter an expression: "))
print(result)

# Accessing error messages
try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code
