t1 = 1, 2, 3, 4, 5, 6
t2 = 7, 8, 9, 10
t3 = 11, 12, 13, 14, 15, 16, 17

concatenated_tuple = t1 + t2 + t3

result = tuple(0 if x % 2 != 0 else x for x in concatenated_tuple)

print("Concatenated tuple with odd values replaced by zeros:", result)
