#Classes for the main app
import csv
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

    def data_dictionary(self, data):
        self.data_dic = {}
        for counter, value in enumerate(data, 1):
            self.data_dic[counter] = value
        return self.data_dic    

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
        return data_dic[self.name_tag]


    def choose_drink(self, data_dic, drinks):
        chosen_drink = True
        while chosen_drink:
            drink_table = table('DRINKS', drinks)
            self.drink_tag = int(input("Please select a drink using a number: "))
            if self.drink_tag not in data_dic.keys():
                print("\nThere are only so many drinks available, try again.")
                # potential check for number 0 input here.
            else:
                chosen_drink = False
                                                    
        return data_dic[self.drink_tag]

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

    def person_details(self):

        self.first_name = input("What is the person's first name?: ")

        self.surname - input("What is the person's surname?: ")

        self.age = int(input("What is the person's age?: "))

        
        
    