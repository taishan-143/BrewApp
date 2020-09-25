def table_width(header, data):
    biggest = len(header)
    for item in data:
        if len(item) > biggest:
            biggest = len(item)
    return biggest + 2


def table(header, data):
    separator = '+' + '='*table_width(header, data) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header)-1) + '|')
    print(separator)
    for item in data:            
        print('|' + ' ' + item + ' '*(table_width(header, data)-len(item)-1) + '|')
    print(separator)