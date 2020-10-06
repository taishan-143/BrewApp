import pymysql
from src.classes.app_classes import Round, Preferences, Person, Drink
from src.functions.table_function import table, table_width 

def assign_preference(people_dic, drinks_dic, people, drinks): 
    selected_name = []                                                              # list to check no multiple assignments occur 
    not_chosen_preference = True
    while not_chosen_preference:  
        new_preference = Preferences()
        Name = new_preference.choose_name(people_dic, selected_name, people)        # get a person from the names file
        Drink = new_preference.choose_drink(drinks_dic, drinks)                     # get a drink from the drinks file

        new_preference.add_to_database(Name, Drink)
        not_chosen_preference = new_preference.add_another()  

        selected_name.append(Name)
    
# To solve overwriting issue:
# Append to pre-existing preferences dictionary
# delete repeat values. 

# edit preferences display to grab persons drink ID and the drink!

def preferences_display(header, data):                           
    items = [] 
    [items.append(f"{name}'s favourite drink: {data[name]}") for name in data.keys()]
    table(header, items)




def Load_People():
    connection = pymysql.connect(
        host = 'localhost',
        port = 33066, 
        user = 'root', 
        passwd = 'Qazwsx11',
        database = "Brew_App"
        )
    cursor = connection.cursor()
    cursor.execute("SELECT PersonID, Person_First_Name, Person_Surname FROM Person")
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

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


def continue_operation(header, action):
    if header == 'DRINKS':
        item = 'drink' 
    else:
        item = 'person'
    not_chosen_option = True
    while not_chosen_option:
        option = input(f"Would you like to {action} another {item}, Y or N?:  ").title()
        if option == 'Y':
            return True
            not_chosen_option = False
        elif option == 'N':
            return False
            not_chosen_option = False
        else:
            print("Sorry, I don't understand")
            not_chosen_option = True

def add_person(header):
    not_added_person = True
    while not_added_person:
        person = Person()
        person_data = person.input_person()
        person.save_person_to_database(person_data)
        print(f"Successfully added {person_data[0]} to the app!")
        not_added_person = continue_operation(header, 'add')

def remove_person(header, data):
    not_removed_person = True
    while not_removed_person:
        person = Person()
        table(header, data)
        name = person.remove_person_from_database(data)
        print(f"Goodbye {name}! See you soon!")
        not_removed_person = continue_operation(header, 'remove')

def add_drink(header):
    not_added_drink = True
    while not_added_drink:
        drink = Drink()
        drink_name = drink.input_drink()
        alcoholic_drink = drink.is_alcoholic()
        drink.save_drink_to_database(drink_name, alcoholic_drink)
        not_added_drink = continue_operation(header, 'add')

def remove_drink(header, data):
    not_removed_drink = True
    while not_removed_drink:
        drink = Drink()
        table(header, data)
        deleted_drink = drink.remove_drink_from_database(data)
        print(f"You have removed {deleted_drink} from the list of drinks")
        not_removed_drink = continue_operation(header, 'remove')


# SORT OUT AUTO INCREMENT ISSUE!!
