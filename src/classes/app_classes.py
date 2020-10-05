#Classes for the main app
import csv
import pymysql
from src.functions.table_function import table, table_width

class Round:
    def __init__(self, people, drinks):
        self.people = people 
        self.drinks = drinks
        self.person_tag = ''
        self.drink_tag = ''
        not_chosen_owner = True
        while not_chosen_owner:
            self.owner = input("Who's round is it?: ").title()
            if self.owner == '' or self.owner == ' ':
                print("Sorry, I dont understand")
                not_chosen_owner = True
            else:
                not_chosen_owner = False


    def order(self, people, drinks):
        order_dic = {}
        # pick person and corresponding fave drink
        dic_generator = Preferences()
        round_order = True
        while round_order:
            people_dic = dic_generator.data_dictionary(people)                         # create people dictionary
            name_table = table('PEOPLE', people)
            not_chosen_person = True
            while not_chosen_person:
                self.person_tag = int(input("Please choose a person: "))
                if self.person_tag not in people_dic.keys():
                    print("You're out of range, try again.")
                else:
                    not_chosen_person = False

            drinks_dic = dic_generator.data_dictionary(drinks)                         # create drinks dictionary
            drinks_table = table('DRINKS', drinks)
            not_chosen_drink = True
            while not_chosen_drink:
                self.drink_tag = int(input("Select that person's drink order: "))
                if self.drink_tag not in drinks_dic.keys():
                    print("You're out of range, try again.")
                else:
                    not_chosen_drink = False
            # CREATE CHECK AGAINST REPEAT PREFERENCE!
            not_chosen_option = True
            while not_chosen_option:
                option = input("Would you like to add another drink to the order, Y or N?: ")
                if option == 'y' or option == 'Y':
                    round_order = True
                    not_chosen_option = False
                elif option == 'n' or option == 'N':
                    round_order = False
                    not_chosen_option = False
                else:
                    print("Sorry, I don't understand.")
                    not_chosen_option = True
            
            order_dic[people_dic[self.person_tag]] = drinks_dic[self.drink_tag]
            people.pop(self.person_tag - 1)                     # (-1) --> Account for index position
        return order_dic
            

    def print_round(self, dictionary):
        print("\n")
        items = []
        for person in dictionary.keys():
            items.append(f"{person} wants to drink a {dictionary[person].title()}.")
        table(f"{self.owner}'s Round", items)

class Preferences:                                                                            # choose a person and a corresponding favourite drink
    def __init__(self):
        self.name_tag = ''                                                                       # start with empty sting, will be overwritten by names list
        self.drink_tag = ''                                                                      # same as above but for drinks 

    def choose_name(self, data_dic, selected_name, people):
        chosen_name = True
        while chosen_name:
            name_table = table('PEOPLE', people)
            self.name_tag = int(input("\nChoose a person from the list using a number: "))
            if self.name_tag not in data_dic.keys():                                                     # checks input against the string of the first name
                print(f"\nNot that many people are present, try again.")
            elif data_dic[self.name_tag] in selected_name:
                print("\nThat person has been selected, pick another person.")
            else:
                chosen_name = False

            people.pop(self.name_tag - 1)                                                     # Account for index position
            person_name = data_dic[self.name_tag]
            person_first_name = person_name.split()[0]

        chosen_name = True
        return person_first_name

    def choose_drink(self, data_dic, drinks):
        chosen_drink = True
        while chosen_drink:
            drink_table = table('DRINKS', drinks)
            self.drink_tag = int(input("Please select a drink using a number: "))
            if self.drink_tag not in data_dic.keys():
                print("\nThere are only so many drinks available, try again.")
                chosen_drinkj = True
                # potential check for number 0 input here.
            else:
                chosen_drink = False
        chosen_drink = True                                        
        return self.drink_tag

    def add_to_database(self, person_name, drinkID):
        try:
            args = (drinkID, person_name)
            connection = pymysql.connect(
                host = 'localhost',
                port = 33066, 
                user = 'root', 
                passwd = 'Qazwsx11',
                database = "Brew_App"
                )
            cursor = connection.cursor()
            cursor.execute("UPDATE Person SET Favourite_Drink = %s WHERE Person_First_Name = %s", args)
            connection.commit()
            cursor.close()
        except Exception:
            print("Failure uploading to the database!")
        finally:
            connection.close()

    def add_another(self):
        not_chosen_option = True
        while not_chosen_option:
            option = input("Would you like to add another preference, Y or N?: ")
            # CHECK THAT THERE ARE PEOPLE TO ADD A PREFERENCE FOR!
            if option == '':
                continue
            
            if option[0] == 'y' or option[0] == 'Y':
                not_chosen_option = False
                not_chosen_preference = True
            elif option[0] == 'n' or option[0] == 'N':
                not_chosen_option = False
                not_chosen_preference = False
            else:
                print("Sorry, I don't understand!")
                not_chosen_option = True
                not_chosen_preference = True
        
        return not_chosen_preference



class Person:
    def __init__(self):
        self.first_name = ''
        self.surname = ''
        self.age = ''
        self.preference = ''

    def input_person(self):
        not_added_data = True
        while not_added_data:
            not_added_fname = True
            while not_added_fname:
                self.first_name = input("What is the person's first name?: ").title()
                if self.first_name == '':
                    print("Sorry, I dont understand")
                    not_added_fname = True
                else: 
                    not_added_fname = False
                    not_added_data = True

            not_added_surname = True
            while not_added_surname:
                self.surname = input("What is the person's surname?: ").title()
                if self.surname == '':
                    print("Sorry, I dont understand")
                    not_added_surname = True
                else:
                    not_added_surname = False
                    not_added_data = True
            
            not_added_age = True
            while not_added_age:
                self.age = int(input("What is the person's age?: "))
                if type(self.age) != int:
                    print("That is not a number, try again")
                    not_added_age = True
                elif self.age == '':
                    print("Sorry, I dont understand")
                    not_added_age = True
                else:
                    not_added_age = False
                    not_added_data = True

            person_data = (self.first_name, self.surname, self.age)
            not_added_data = False
        return person_data
    
    def save_person_to_database(self, person_data):
        try:
            connection = pymysql.connect(
                host = 'localhost',
                port = 33066, 
                user = 'root', 
                passwd = 'Qazwsx11',
                database = "Brew_App"
                )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Person (Person_First_Name, Person_Surname, Person_Age) VALUES (%s, %s, %s)", person_data)
            connection.commit()
            cursor.close()
        except Exception:
            print("Failure uploading to the database!")
        finally:
            connection.close()

    def remove_person_from_database(self, data):
        not_removed_person = True
        while not_removed_person:
            personID = int(input("Choose a person to remove: "))
            if type(personID) != int:
                print("That is not a number, try again")
                not_removed_person = True
            elif personID == '':
                print("Sorry, I don't Understand!")
                not_removed_person = True
            else:
                not_removed_person = False
            
            name = data.pop(personID-1)
            first_name = name.split()[0]

        try:
            connection = pymysql.connect(
                host = 'localhost',
                port = 33066, 
                user = 'root', 
                passwd = 'Qazwsx11',
                database = "Brew_App"
                )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Person WHERE Person_First_Name = %s", first_name)
            connection.commit()
            cursor.close()
        except Exception:
            print("Failure removing from the database!")
        finally:
            connection.close()
        
        return first_name
        
class Drink:
    def __init__(self):
        self.drink_name = ''
        self.alcoholic = ''

    def input_drink(self):
        not_added_drink = True
        while not_added_drink:
            self.drink_name = input("What is the name of the drink?: ").title()
            if type(self.drink_name) != str:
                print("That doesn't make sense, try again")
                not_added_drink = True
            elif self.drink_name == '':
                print("Sorry, I don't understand")
                not_added_drink = True
            else:
                not_added_drink = False

        return self.drink_name

    def is_alcoholic(self):
        not_validated = True
        while not_validated:
            self.alcoholic = input("Is this drink alcoholic, Y or N?: ").title()  
            if type(self.alcoholic) != str:
                print("That doesn't make sense to me, try again")  
                not_validated = True
            elif self.alcoholic == '':
                print("Sorry, I don't understand")
                not_validated = True
            else:
                not_validated = False      
            
        if self.alcoholic == 'Y':
            alcoholic = 1
        elif self.alcoholic == 'N':
            alcoholic = 0

        return alcoholic
    
    def save_drink_to_database(self, input_drink, is_alcoholic):
        drink_data = (input_drink, is_alcoholic)
        try:
            connection = pymysql.connect(
                host = 'localhost',
                port = 33066, 
                user = 'root', 
                passwd = 'Qazwsx11',
                database = "Brew_App"
                )
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Drinks (DrinkName, Alcoholic) VALUES (%s, %s)", drink_data)
            connection.commit()
            cursor.close()
        except Exception:
            print("Failure uploading to the database!")
        finally:
            connection.close()

    def remove_drink_from_database(self, data):
        not_removed_drink = True
        while not_removed_drink:
            drinkID = int(input("Choose a drink to remove: "))
            if type(drinkID) != int:
                print("That doesn't make any sense, try again")
                not_removed_drink = True
            elif drinkID == '':
                print("Sorry, I dont understand")
                not_removed_drink = True
            else:
                not_removed_drink = False

            name = data.pop(drinkID-1)

        try:
            connection = pymysql.connect(
                host = 'localhost',
                port = 33066, 
                user = 'root', 
                passwd = 'Qazwsx11',
                database = "Brew_App"
                )
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Drinks WHERE DrinkID = %s", drinkID)
            connection.commit()
            cursor.close()
        except Exception:
            print("Failure removing from the database!")
        finally:
            connection.close()
        
        return name
            







        
    