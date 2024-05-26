phone = input('phone: ')

numbers_dict = {
    "0": "zero ",
    "1": "one ",
    "2": "two ",
    "3": "three ",
    "4": "four ",
    "5": "five ",
    "6": "six ",
    "7": "seven ",
    "8": "eight ",
    "9": "nine ",
    "10": "ten "
}
for digits in phone:
    print(numbers_dict.get(digits, "(not a number!) "), end='')