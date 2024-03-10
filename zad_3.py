def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = range(1, 11)
print_even_numbers(numbers)
