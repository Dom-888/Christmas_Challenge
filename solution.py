def christmas_tree():
    for i in range(14):
        left_space = (14 - i) * ' '
        plain_segment = '/' + ((i * 2) - 1) * ' ' + '\\'
        edged_segment = '/_' + ((i * 2) - 3) * ' ' + '_\\'
        
        #Tip
        if i == 1:
            print(left_space + ' |')
            print(left_space + plain_segment)

        #Center
        elif (i + 0) % 2 != 0 and i != 13:
            print(left_space + edged_segment)
            print(left_space + plain_segment)
        elif (i + 0) % 2 == 0 and i > 1:
            print(left_space + plain_segment)

        #Bottom
        elif i == 13:
            print(left_space + plain_segment)
            print('|' + ('_' * 27) + '|')
            print((' ' * 11) + '\\' + ('_' * 7) + '/')

