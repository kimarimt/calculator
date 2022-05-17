import os
import time


operations = {
    '+': lambda num1, num2: num1 + num2,
    '-': lambda num1, num2: num1 - num2,
    '*': lambda num1, num2: num1 * num2,
    '/': lambda num1, num2: num1 / num2,
}


def clear():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    again = ''
    result = 0
    previous_result = 0

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
            previous_result = result
            operation = input('Pick an operation: ')
            next_number = float(input('Enter the next number: '))
            result = operations[operation](result, next_number)
            print(f'{previous_result} {operation} {next_number} = {result}')
            clear()


if __name__ == '__main__':
    main()
