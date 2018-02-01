rows = int(input('How tall will the tree be: '))
for i in range(rows):
    print(' ' * (rows - i - 1) + '#' * (2 * i + 1))
print( (((rows-1)*' ') + '#'))