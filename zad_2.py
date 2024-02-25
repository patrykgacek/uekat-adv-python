def multiply_by_two_v1(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

numbers = range(1, 6)


def multiply_by_two_v2(numbers):
    return [number * 2 for number in numbers]


numbers = range(1, 6)

result = multiply_by_two_v1(numbers)
print(result)

result = multiply_by_two_v2(numbers)
print(result)
