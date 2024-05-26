numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9, 7, 8, 3, 5]
uniques =[]
for digits in numbers:
    if digits not in uniques:
        uniques.append(digits)
print(uniques)
