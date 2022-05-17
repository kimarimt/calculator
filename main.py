operations = {
    '+': lambda num1, num2: num1 + num2,
    '-': lambda num1, num2: num1 - num2,
    '*': lambda num1, num2: num1 * num2,
    '/': lambda num1, num2: num1 / num2,
}


def main():
    again = ''
    result = 0

    while True:
        if again == 'n' or again == '':
            first_number = float(input('Enter the first number: '))
            print('+, -, *, /')
            operation = input('Pick an operation: ')
            second_number = float(input('Enter the next number: '))
            result = operations[operation](first_number, second_number)
            print(f'{first_number} {operation} {second_number} = {result}')

        again = input(
            f'Type \'y\' to continue with {result}, or \'n\' to start a new calculation: ')
        if again == 'y':
            operation = input('Pick an operation: ')
            next_number = float(input('Enter the next number: '))
            result = operations[operation](result, next_number)
            print(f'{result} {operation} {next_number} = {result}')


if __name__ == '__main__':
    main()
