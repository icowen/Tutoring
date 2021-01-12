# Example:
person = input('Enter your name: ')
print('Hello', person)
print('Hello' + person)
print('Hello ' + person)
while input('Press enter to continue') != '\n':
    continue

# If passed a value to sep, that value you SEParate each parameter passed to print
print('Hello', person, sep='')
print('Hello', person, ', and', sep=' mister ')

# If we want to get a different type, we have to convert the input to that type
# x =