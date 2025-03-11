number1 = float(input('Enter your first number:'))
number2 = float(input('Enter your second number:'))
operation = input("Enter your symbol '+,-,*,/':")

if operation == '+' :
    result = number1 + number2
    print(f'{number1} + {number2} = {result}')
elif operation == '-' :
    result = number1 - number2
    print(f'{number1} - {number2} = {result}')
elif operation == '*' :
    result = number1 * number2
    print(f'{number1} * {number2} = {result}')
elif operation == '/' :
    result = number1 / number2
    print(f'{number1} / {number2} = {result}')
else:
    print('Invalid Operation')