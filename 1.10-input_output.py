# Example:
person = input('Enter your name: ')
print('Hello', person)
print('Hello' + person)
print('Hello ' + person)
while input('Press enter to continue') != '':
    continue
print()

# If passed a value to sep, that value you SEParate each parameter passed to print
print('Hello', person, sep='')
print('Hello', person, sep=' ')
print('Hello', person, ', and', person, sep=' mister ')
while input('Press enter to continue') != '':
    continue
print()

# If we want to get a different type, we have to convert the input to that type
x = input('Enter a number: ')
y = input('Enter another number: ')
print(f'{x} + {y} = {x+y}')
print(f'{x} + {y} = {int(x)+int(y)}')
print(f'{x} + {y} = {float(x)+float(y)}')
while input('Press enter to continue') != '':
    continue
print()

# -----------EXERCISE----------------

# Write a version, add3.py, that asks for three numbers,
# and lists all three, and their sum, in similar format to that displayed above.

# Write a program, quotient.py, that prompts the user for two integers,
# and then prints them out in a sentence with an integer division problem in a form just like:
# "The quotient of 14 and 3 is 4 with a remainder of 2"

# Repeat both exercises above using string formatting f'{}' in files named
# add3f.py and quotientformat.py


