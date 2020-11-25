import pymysql
import os
from src.classes.app_classes import Round, Preferences, Person, Drink
from src.functions.table_function import table, table_width 

def assign_preference(people_dic, drinks_dic): 
    selected_name = []               # list to check no multiple assignments occur 
    preferences = {}
    not_chosen_preference = True
    while not_chosen_preference:  
        new_preference = Preferences()
        NameID = new_preference.choose_name(people_dic, selected_name)        # get a person from the names file
        DrinkID = new_preference.choose_drink(drinks_dic)                     # get a drink from the drinks file

        #first_name = Name.split()[0]   # Take the first name for database use
        new_preference.add_to_database(NameID, DrinkID)  # add the preference to the database
        if len(selected_name) == len(people_dic.keys()):
            break
        else:
            not_chosen_preference = new_preference.add_another()   # give an option to add another

        
        preferences[people_dic[NameID]] = drinks_dic[DrinkID]
        selected_name.append(NameID) 
        people_dic.pop(NameID)       
        
    return preferences

def access_preferences():
    try:
        connection = pymysql.connect(
            host = 'localhost',
            port = 33068, 
            user = 'root', 
            passwd = 'Qazwsx11',
            database = "Brew_App"
            )
        cursor = connection.cursor()
        cursor.execute("SELECT Person.Person_First_Name, Drinks.DrinkName FROM Person INNER JOIN Drinks ON Person.Favourite_Drink = Drinks.DrinkID")
        data = cursor.fetchall()
        connection.commit()
        cursor.close()
    except Exception:
        print("Failure reading from the database")
    finally:
        connection.close()
    return data

def display_preferences(data):
    preferences = []
    for items in data:
        name, drink = items[0], items[1]
        preference = f"{name}'s favourite drink: {drink}"
        preferences.append(preference)
    table('PREFERENCES', preferences)


def Load_People():
    # Establish connection to MySQL Database
    try:
        connection = pymysql.connect(
            host = 'localhost',
            port = 33068, 
            user = 'root', 
            passwd = 'Qazwsx11',
            database = "Brew_App"
            )
        cursor = connection.cursor()
        # Select the person data
        cursor.execute("SELECT PersonID, Person_First_Name, Person_Surname FROM Person")
        connection.commit()
        rows = cursor.fetchall()
        cursor.close()
    except Exception as ERROR:
        print("Execution Issue: " + str(ERROR))
    finally:
        connection.close()

    # Generate the dictionary of: {person_ID:'person_full_name'}
    people_dic_list = []
    for row in rows:
        list_row = list(row)
        fname = list_row.pop(1)
        sname = list_row.pop(1)
        name = list_row.insert(1, (fname + ' ' + sname))
        people_dic_list.append(tuple(list_row))

    people_dic = dict(people_dic_list)
    return people_dic

def Load_Drinks():
    connection = pymysql.connect(
        host = 'localhost',
        port = 33068, 
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


def continue_operation(message):
    not_chosen_option = True
    while not_chosen_option:
        option = input(message + ", Y or N?:  ").title()
        if option == 'Y':
            return True
            not_chosen_option = False
        elif option == 'N':
            return False
            not_chosen_option = False
        else:
            print("\nSorry, I don't understand")
            not_chosen_option = True

def add_person(header):
    not_added_person = True
    while not_added_person:
        person = Person()
        person_data = person.input_person()
        person.save_person_to_database(person_data)
        print(f"Successfully added {person_data[0]} to the app!")
        not_added_person = continue_operation("\nWould you like to add another person")

def remove_person(header, data):
    not_removed_person = True
    while not_removed_person:
        if len(data.values()) == 0:
            print("\nThere are no people to remove")
            break
        else:
            person = Person()
            table(header, data)
            name = person.remove_person_from_database(data)
            print(f"Goodbye {name}! See you soon!")
            if len(data.values()) > 0:
                not_removed_person = continue_operation("\nWould you like to remove another person")
            else:
                print("All people have been removed!")
                not_removed_person = False

def add_drink(header):
    not_added_drink = True
    while not_added_drink:
        drink = Drink()
        drink_name = drink.input_drink()
        alcoholic_drink = drink.is_alcoholic()
        drink.save_drink_to_database(drink_name, alcoholic_drink)
        not_added_drink = continue_operation("\nWould you like to add another drink")

def remove_drink(header, data):
    not_removed_drink = True
    while not_removed_drink:
        if len(data.values()) == 0:
            print("\nThere are no drinks to remove")
            break
        else:
            drink = Drink()
            table(header, data)
            deleted_drink = drink.remove_drink_from_database(data)
            print(f"You have removed {deleted_drink} from the list of drinks")
            if len(data.values()) > 0:
                not_removed_drink = continue_operation("\nWould you like to remove another drink")
            else:
                print("All drinks have been removed!")
                not_removed_drink = False

def clear():
    os.system("clear")

def connect_to_database():
    connection = pymysql.connect(
        host = 'localhost',
        port = 33068, 
        user = 'root', 
        passwd = 'Qazwsx11',
        database = "Brew_App"
        )
    cursor = connection.cursor()
    print("Connected to the database")

