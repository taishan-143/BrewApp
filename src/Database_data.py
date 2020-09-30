import pymysql

def Person_DB():
    connection = pymysql.connect(
        host = 'localhost',
        port = 33066, 
        user = 'root', 
        passwd = 'Qazwsx11',
        database = "Brew_App"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT PersonID, Person_Name FROM Person")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    people_dic_list = []
    for row in rows:
        people_dic_list.append(row)
        people_dic = dict(people_dic_list)

    return people_dic


# filter the data needed
# replace csv data persistence with database management
# refactor code for database management


def Drink_DB():
    connection = pymysql.connect(
        host = 'localhost',
        port = 33066, 
        user = 'root', 
        passwd = 'Qazwsx11',
        database = "Brew_App"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT DrinkID, DrinkName FROM Drinks")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    drinks_dic_list = []
    for row in rows:
        drinks_dic_list.append(row)
        drinks_dic = dict(drinks_dic_list)

    return drinks_dic
    


# people_DIC = Person_DB()
# print("\n")
# drinks_DIC = Drink_DB()