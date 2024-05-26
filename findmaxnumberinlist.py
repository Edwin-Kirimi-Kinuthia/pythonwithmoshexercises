numbers = [1,2,2,3,6,8,9,10,6,8,80,90]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)