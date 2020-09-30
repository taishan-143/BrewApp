import pymysql


class Person:
    def __init__(self):
        pass

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

    for row in rows:
        people_dic = {}
        ID, Name = PersonID, Person_Name
        people_dic[ID] = Name



def Drink_DB():
    connection = pymysql.connect(
        host = 'localhost',
        port = 33066, 
        user = 'root', 
        passwd = 'Qazwsx11',
        database = "Brew_App"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT DrinkName, Alcoholic FROM Drinks")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    for row in rows:
        people_dic_list = []
        people_dic_list.append(row)
        people_dic = dict(people_dic_list)


Person_DB()
print("\n")
#Drink_DB()