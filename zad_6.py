def merge_and_pow3_lists(list1: list, list2: list) -> list:
    merged = list(set(list1 + list2))
    return [n ** 3 for n in merged]


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = merge_and_pow3_lists(list1, list2)
print(result)
