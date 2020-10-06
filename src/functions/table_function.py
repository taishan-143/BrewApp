def table_width(header, data):
    biggest = len(header)
    if data == [] or data == ' ':
        return biggest + 2
    else:
        for key, value in enumerate(data, 1):
            if value == '':
                continue
            elif len(str(value)) > biggest:
                biggest = len(str(value))
        return biggest + len(str(key)) + 5


def table(header, data):
    separator = '+' + '='*table_width(header, data) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header)-1) + '|')
    print(separator)
    for key, value in enumerate(data, 1):          
        print('|' + ' ' + f"[{str(key)}]" + ' ' + str(value) + ' '*(table_width(header, data)-len(str(key))-len(str(value))-4) + '|')
    print(separator)

    # ONLY HANDLING LISTS!!! CHANGE TO FIT!!!