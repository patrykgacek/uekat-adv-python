def print_every_second_element(elements):
    for i in range(1, len(elements), 2):
        print(elements[i])


numbers = range(1, 11)
print_every_second_element(numbers)
