def table_width(header, data):     # calculates the width of the table needed for a perfect fit
    biggest = len(header) 
    if data == [] or data == ' ':
        return biggest + 2
    elif type(data) == list:      # only preference display used for this :- +2 accounts for end spaces
        for item in data:
            if item == '':
                continue
            elif len(item) > biggest:
                biggest = len(item)
        return biggest + 2
    else:                           # used for all other data :- +5 used for end spaces and square brackets
        for key, value in data.items():
            if value == '':
                continue
            elif len(str(value)) + len(str(key)) > biggest:
                biggest = len(str(value)) + len(str(key))
        return biggest + 5
            

def table(header, data):                            
    separator = '+' + '='*table_width(header, data) + '+'
    print('\n' + separator)
    print(f'| {header}' + ' '*(table_width(header, data)-len(header)-1) + '|')
    print(separator)
    if type(data) == dict:
        for key, value in data.items():          
            print('|' + ' ' + f"[{str(key)}]" + ' ' + str(value) + ' '*(table_width(header, data)-len(str(key))-len(str(value))-4) + '|')
    else:
        for item in data:
            print('|' + ' ' + item + ' '*(table_width(header, data)-len(item)-1) + '|')
    print(separator)

def recipts(header, order_time, data):
    recipt_header = f"{header}" + ' '*5 + 'ORDER RECIPT' + ' '*5 + f"{order_time}"
    separator = '+' + '='*table_width(recipt_header, data) + '+'
    print('\n' + separator)
    print("|" + ' ' +  recipt_header + ' '*(table_width(recipt_header, data)-len(recipt_header)-1) + '|')
    print(separator)
    for name, drink in data.items():
        print('|' + ' ' + f"{name} ordered a {drink}" + ' '*(table_width(recipt_header, data)-len(name)-len(drink)-12) + '|')
    print(separator)

    