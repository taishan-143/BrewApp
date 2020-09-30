import csv
import pymysql

# username = 1st, name = 2nd (split into first and last) 
# job title = 4th, mobile = 8th, zip = 13th


def data_extraction(filepath):     # load the csv file
    data_list = []
    try:
        with open(filepath, 'r') as data_file:
            line_reader = csv.reader(data_file)
            for line in line_reader:
                data = []
                data.extend([line[0], line[1], line[3], line[7], line[12]])  # extract the data needed
                data_list.append(data)
            return data_list
    except Exception:
        print("Failure opening file!")
    

db_data = data_extraction('src/data/Import_User_Sample_en.csv')

    
def data_transformation(data):
    final_data = []

    for data_list in data[:1]:
        if data_list[1] == 'Name':
            data_list[1] = 'First Name'
            data_list.insert(2, 'Surname')
        # final_data.append(data_list)
        continue

    for data_list in data[1:]:
        first_name = data_list[1].split()[0].title()
        surname = data_list[1].split()[1].title()
        data_list.pop(1)
        data_list.insert(1, first_name)
        data_list.insert(2, surname)
        final_data.append(data_list)

    return final_data
    

data_transform = data_transformation(db_data)
print(data_transform)

def data_loading_to_the_database(data):
    connection = pymysql.connect(
        host = 'localhost',
        port = 33066, 
        user = 'root', 
        passwd = 'Qazwsx11',
        database = "Brew_App"
        )
    cursor = connection.cursor()
    for person_data in data:
        #print(tuple(person_data))
        cursor.execute("INSERT INTO PersonImport (User_Name, First_Name, Surname, Job_Title, Mobile_No, Post_Code) VALUES (%s, %s, %s, %s, %s, %s)", person_data)

    connection.commit()
    # rows = cursor.fetchall()
    cursor.close()
    connection.close()

data_loading_to_the_database(data_transform)










# def save_items_to_csv(filepath, data):
#     try:
#         with open(filepath, 'w', newline ='') as data_file:
#             csv_writer = csv.writer(data_file, quoting = csv.QUOTE_NONE)
#             for item in data:
#                 csv_writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5]])
#     except:
#         print("Failure opening file!")

# save_items_to_csv('src/data/Upload_to_database.csv', data_transform)








