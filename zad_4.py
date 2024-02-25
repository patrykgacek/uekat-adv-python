def is_sum_greater_or_equal(a: int, b: int, c: int) -> bool:
    return a + b >= c


a = 1
b = 2
c = 3
result = is_sum_greater_or_equal(a, b, c)
print(f'Is {a} + {b} greater or equal to {c}? {result}')
