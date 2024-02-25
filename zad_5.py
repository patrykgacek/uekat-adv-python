def is_value_in_list(list: list, value: int) -> bool:
    return value in list


list = [1, 2, 3, 4, 5]
value = 4
result = is_value_in_list(list, value)
print(f'Is "{value}" in {list}? {result}')
