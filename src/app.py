# Author:         Taishan Rowe
# Last Modified:  17/09/2020

import os
import csv
from table_function import table, table_width#    # Importing the table
import save_load as S_L

os.system("clear")

# PLANS FOR EXTRA FUNCTIONALITY:

# Find way to select people efficiently - maybe use numbering system or name initials
# Potentially -- add age func/class
# DONE: Check against favourite drink
# Ask if they'd like to add another preference, by name.

# Classes

# creating a class to take a round of drinks
class Round:
    def __init__(self, people, drinks, round_owner):
        self.people = people 
        self.drinks = drinks
        self.owner = round_owner
        

    def drinks_order(self, data):                                                          # data is a preferences dictionary
        round_order = True
        order_dict = {}
        while round_order:   
            for person in self.people:                                                     # each person runs through for loop and wile loop
                not_correct_order = True                                                   # to choose a drink. While loop used to check if drink is available.
                while not_correct_order:
                    order = input(f"\nWhat would {person} like to drink?: ")
                    if order.title() not in self.drinks:
                        print("That drink isn't available, choose again please.")
                        not_correct_order = True
                    elif order.title() == data[f"{person}"]:                                # if the order is that persons favourite, 
                        not_correct_order = False                                           # continue
                    elif order.title() != data[f"{person}"]:                                # if the order isn't that persons favourite,
                        print(f"{person.split()[0]} prefer's to drink {data[person]}")      # notify and give an option to select the favourite
                        incorrect_option = True
                        while incorrect_option:
                            choice = input(f"Would you like to order {data[person]} instead? (Y or N): ")
                            if choice == 'y' or choice == 'Y':                              # loop for the option to choose favourite drink or not
                                order = data[f"{person}"]
                                incorrect_option = False
                                not_correct_order = False
                            elif choice == 'n' or choice == 'N':                            # incorrect_option, round_order and not_correct_order act as on and off switches for the while loops
                                incorrect_option = False                                    # on = True, off = False
                                not_correct_order = False
                            else:
                                print("Sorry, I dont understand:")
                                incorrect_option = True
                                not_correct_order = True
                    else:
                        not_correct_order = False
                        round_order = False            
                    order_dict[f"{person}"] = f"{order}"                                   # dictionary of orders to be generated and returned
            round_order = False
        return order_dict

    def print_round(self, dictionary):
        print("\n")
        items = []
        for person in dictionary.keys():
            items.append(f"{person} wants to drink a {dictionary[person].title()}.")
        table(f"{self.owner}'s Round", items)

class People:                                                                              # generate a list of people from a file
    def __init__(self):
        self.people = []
    
    def load_people(self, filepath):
        with open(filepath, "r") as persons:
            [self.people.append(line.strip()) for line in persons.readlines() if not line.isspace()]  # removes new line indicator and spaces
        return self.people
    
class Drinks:                                                                               # generate a list of drinks from a file
    def __init__(self):
        self.drinks = []
    
    def load_drinks(self, filepath):
        with open(filepath, "r") as all_drinks:
            [self.drinks.append(line.strip()) for line in all_drinks.readlines() if not line.isspace()]  # removes new line indicator and spaces
        return self.drinks

class Preferences:                                                                           # choose a person and a corresponding favourite drink
    def __init__(self):
        self.name = ''                                                                       # start with empty sting, will be overwritten by names list
        self.drink = ''                                                                      # same as above but for drinks
         

    def choose_name(self, people, selected_name):                                            # person input
        chosen_name = True
        while chosen_name:
            table('PEOPLE', people)
            self.name = input("\nChoose a person from the list: ").title()
            if self.name not in people:                                                     # checks input against the string of the first name
                print(f"\n{self.name} isn't on the list, try again.")
            elif self.name in selected_name:
                print("\nThat person has already been selected, try again.")
            else:
                chosen_name = False
        return self.name

    def choose_drink(self, drinks):                                                         # corresponding favourite drink input 
        chosen_drink = True
        while chosen_drink:
            table('DRINKS', drinks)
            self.drink = input(f"\nWhat is their favourite drink?: ").title()
            if self.drink not in drinks:
                print(f"\n{self.drink} isn't on the menu, try again.")
            else:
                chosen_drink = False
        return self.drink

# def load_people_csv(filepath):                                                              # load via csv file
#     new_people = []
#     with open(filepath, 'r') as csv_people:
#         line_reader = csv.reader(csv_people)
#         separator = ' '
#         for line in line_reader:
#             joined_line = separator.join(line)
#             new_people.append(joined_line)

#     return new_people

# # Add to the lists

def add_to_table(header, data):
    add_more = True
    add_new = True
    while add_new:
        # checks for people or drinks
        if data == drinks:
            item = 'drink'
        else:
            item = 'person'
        # ask user for data input 
        new_data = input(f"\nPlease add a new {item} to the list: ").title()
        # append input to the data list
        data.append(new_data)
        # ask user again whether they want to input more
        while add_more:
            choice = input(f"Do you want to add more {header.lower()}, Y or N?: ")
            if choice[0] == 'N' or choice[0] == 'n':
                print("\nThank you!")
                add_more = False
                add_new = False
            elif choice[0] == 'Y' or choice[0] == 'y':
                add_more = False
                add_new = True
            else:
                print("\nSorry, I dont understand!")
        add_more = True

# Save the new additions to the lists

# def save_items(filepath, data):                                                  # for .txt files
#     try:
#         with open(filepath, 'w') as data_file:    
#             [data_file.write(item + '\n') for item in data]
#     except:
#         print('Failure opening file!') 

# def save_data(filepath, data):                                                  # for .txt files
#     try:
#         with open(filepath, 'w') as data_file:    
#             [data_file.write(f"{key}:{value}" + '\n') for key, value in data.items()]
#     except:
#         print('Failure opening file!') 

# def save_preferences_csv(filepath, data):      
#     try:
#         with open(filepath, 'w') as csv_data_file:
#             csv_writer = csv.writer(csv_data_file, quoting = csv.QUOTE_ALL)
#             for key, value in data.items():
#                 csv_writer.writerow([key,value])
#     except:
#         print('Failure opening file!')

# # create load preferences function

# def load_preferences(filepath):                                                   # convert list into dictionary - .txt file reader
#     try:
#         with open(filepath, 'r') as file:
#             data = {}
#             for line in file.readlines():
#                 if line =='':
#                     continue
#                 key, value = line.strip().split(':')
#                 data[key.strip()] = value.strip()  
#     except FileNotFoundError as e:
#         e = (f"File '{filepath}' cannot be found")
#         print(e)
#     except Exception as e:
#         e = (f"Unable to open file '{filepath}'.")
#     return data

# def load_preferences_csv(filepath):                                             # .csv file reader
#     try:
#         with open(filepath, 'r') as csv_file:
#             data = {}
#             line_reader = csv.reader(csv_file)
#             separator = ':'
#             for line in line_reader:
#                 if line == []:                                                  # omit empty spaces which are processed as empty lists
#                     continue
#                 data[line[0]] = line[1]
#     except FileNotFoundError as e:
#         e = (f"File '{filepath}' cannot be found")
#         print(e)
#     except Exception as e:
#         e = (f"Unable to open file '{filepath}'.")
#     return data
                

# Assign preferences to people       

def assign_preference(people, drinks): 
    selected_name = []                                                              # list to check no multiple assignments occur 
    drinks_dictionary = {}
    a = 1
    while a <= len(people):
        new_preference = Preferences()                                              # instantiate preference class
        Name = new_preference.choose_name(people, selected_name)                    # get a person from the names file
        Drink = new_preference.choose_drink(drinks)                                 # get a drink from the drinks file
                                                                                    
        chosen_name = True
        chosen_drink = True
        selected_name.append(Name)
        drinks_dictionary[f'{Name}'] = f'{Drink}'
        a+=1
    return drinks_dictionary
    

# Generate a list of preferences 

def preferences_display(header, data):                           
    items = [] 
    [items.append(f"{name}'s favourite drink: {data[name]}") for name in data.keys()]
    table('Preferences', items)
    

# Create the menu with user input

def menu():
    print("""
    Welcome to my wonderful factory of assorted beverages!

    Please select an option: 

    1) View all people
    2) View all drinks
    3) Add people
    4) Add drinks
    5) Favourite drinks selection
    6) Preferences
    7) Drinks order
    8) Exit 
""")

def view_another_page():                                                        # The user decides if they wish to view the menu
    while True:
        choice = input("\nWould you like to view the menu again, Y or N?: ")
        if choice[0] == 'y':
            return choice                                                       # returns True for the app logic
        if choice[0] == 'n':
            return False                                                        # for the app logic
        else:
            print("\nI dont understand.") 
        
# APP LOGIC 
def app_start():
    while True:

        view_menu = True
        menu()                                                                      # show the menu
        people = People().load_people('names.txt')
        #people = load_people_csv('new_names.csv')                                  # Decide on appropriate file type
        #print(people)
        drinks = Drinks().load_drinks('drinks.txt')
        #drinks_preferences = load_preferences('preferences.txt')
        drinks_preferences = S_L.load_preferences_csv('new_preferences.csv')
        #print(drinks_preferences)
        while view_menu:                                                            # Loop for decision making, accounting for mistakes
            #try:    
                option = int(input("\nChoose your selection here (1-8): "))         # user picks their desired page
                if option == 1:
                    table('PEOPLE', people)  
                    view_menu = False
                elif option == 2:
                    table('DRINKS', drinks) 
                    view_menu = False
                elif option == 3:
                    add_to_table('PEOPLE',people)
                    table('PEOPLE',people)
                    save_items('names.txt',people)
                    view_menu = False
                elif option == 4:
                    add_to_table('DRINKS',drinks)
                    table('DRINKS', drinks)
                    save_items('drinks.txt', drinks)
                    view_menu = False
                elif option == 5:
                    drinks_prefs = assign_preference(people, drinks)
                    S_L.save_preferences_csv('new_preferences.csv', drinks_prefs)
                    view_menu = False
                elif option == 6: 
                    preferences_table = preferences_display("PREFERENCES", drinks_preferences)   
                    view_menu = False
                elif option == 7:
                    drinks_round = Round(people, drinks, 'Taishan')
                    beverages = drinks_round.drinks_order(drinks_preferences)
                    drinks_round.print_round(beverages)
                    view_menu = False
                elif option == 8:
                    print("\nThanks for stopping by, see you soon!\n")
                    exit()
                else: 
                    print("\nSorry I dont understand.\nPlease choose between 1 and 8.")
            # except ValueError as v:                                                             # Raised if anything other than an integer is input.
            #     print('\n')
            #     print(v)
            #     print("That is not an integer between 1 and 8, try again!")
            # except NameError as n:                                                              # Raised if the preferences list is opened without 
            #     print('\n')                                                                     # assigning people to drinks
            #     print(n)
                


        if not view_another_page():                                                             # Ending the app
            print("\nThanks for stopping by, see you soon!\n")  # FIX for 'if __name__ == "__main__"' clause!
            break 

if __name__ == "__main__":
    app_start()