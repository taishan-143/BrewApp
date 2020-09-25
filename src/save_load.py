#SAVE FUNCS

def save_items(filepath, data):                                                  # for .txt files
    try:
        with open(filepath, 'w') as data_file:    
            [data_file.write(item + '\n') for item in data]
    except:
        print('Failure opening file!') 

def save_data(filepath, data):                                                  # for .txt files
    try:
        with open(filepath, 'w') as data_file:    
            [data_file.write(f"{key}:{value}" + '\n') for key, value in data.items()]
    except:
        print('Failure opening file!') 

def save_preferences_csv(filepath, data):      
    try:
        with open(filepath, 'w') as csv_data_file:
            csv_writer = csv.writer(csv_data_file, quoting = csv.QUOTE_ALL)
            for key, value in data.items():
                csv_writer.writerow([key,value])
    except:
        print('Failure opening file!')

# LOAD FUNCS

def load_people_csv(filepath):                                                    # load via csv file
    new_people = []
    with open(filepath, 'r') as csv_people:
        line_reader = csv.reader(csv_people)
        separator = ' '
        for line in line_reader:
            joined_line = separator.join(line)
            new_people.append(joined_line)

    return new_people

def load_preferences(filepath):                                                   # convert list into dictionary - .txt file reader
    try:
        with open(filepath, 'r') as file:
            data = {}
            for line in file.readlines():
                if line =='':
                    continue
                key, value = line.strip().split(':')
                data[key.strip()] = value.strip()  
    except FileNotFoundError as e:
        e = (f"File '{filepath}' cannot be found")
        print(e)
    except Exception as e:
        e = (f"Unable to open file '{filepath}'.")
    return data

def load_preferences_csv(filepath):                                             # .csv file reader
    try:
        with open(filepath, 'r') as csv_file:
            data = {}
            line_reader = csv.reader(csv_file)
            separator = ':'
            for line in line_reader:
                if line == []:                                                  # omit empty spaces which are processed as empty lists
                    continue
                data[line[0]] = line[1]
    except FileNotFoundError as e:
        e = (f"File '{filepath}' cannot be found")
        print(e)
    except Exception as e:
        e = (f"Unable to open file '{filepath}'.")
    return data

