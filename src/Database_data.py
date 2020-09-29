import pymysql

def Person_DB():
    connection = pymysql.connect(
        host = 'localhost', 
        port = 33066
        user = 'root', 
        passwd = 'Qazwsx11'
        database = "Person"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT Person_Name, Person_Age FROM Person")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    
    for row in rows:
        print(row)

Person_DB()