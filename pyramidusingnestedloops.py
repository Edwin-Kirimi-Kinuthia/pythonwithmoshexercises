# Number of rows for the upper part of the diamond
num_rows = 5

# Upper part of the diamond (including middle row)
for i in range(1, num_rows + 1):
    # Inner loop for spaces
    for j in range(num_rows - i):
        print(' ', end='')

    # Inner loop for stars
    for k in range(2 * i - 1):
        print('*', end='')

    print()

# Lower part of the diamond
for i in range(num_rows - 1, 0, -1):
    # Inner loop for spaces
    for j in range(num_rows - i):
        print(' ', end='')

    # Inner loop for stars
    for k in range(2 * i - 1):
        print('*', end='')

    print()
