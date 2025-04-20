# numbers = [3, 51, 2, 8, 6]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]




items.sort(key=lambda item: item[1])                                                                                              
print(items)