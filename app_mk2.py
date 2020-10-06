# Author:         Taishan Rowe
# Last Modified:  17/09/2020

import os
import csv
from src.functions.table_function import table, table_width    
import src.classes.save_load as SL
import src.functions.app_methods as AM
import src.classes.app_classes as AC


# PLANS FOR EXTRA FUNCTIONALITY:

# DONE: Find way to select people efficiently - maybe use numbering system or name initials
# Potentially -- add age func/class
# DONE: Check against favourite drink
# DONE: Ask if they'd like to add another preference, by name.
# DONE: Add remove drinks/people functions
    

# Create the menu with user input

def menu():
    print("""
    Welcome to my wonderful factory of assorted beverages!

    Please select an option: 

   +================================+ 
   |          MAIN MENU             |
   +================================+
   | [1] View all people            |
   | [2] View all drinks            |
   | [3] Add people                 |
   | [4] Remove people              |
   | [5] Add drinks                 |
   | [6] Remove drinks              |
   | [7] Favourite drinks selection |
   | [8] Preferences                |
   | [9] Drinks order               |
   | [10] Exit                      |
   +================================+
""")


def view_another_page():                                                        # The user decides if they wish to view the menu
    while True:
        choice = input("\nWould you like to view the menu again, Y or N?: ")
        if choice == '' or choice == ' ':
            continue
        elif choice[0] == 'y' or choice[0] == 'Y':
            return choice                                                       # returns True for the app logic
        elif choice[0] == 'n' or choice[0] == 'N':
            return False                                                        # for the app logic
        else:
            print("\nI dont understand.") 
        
# APP LOGIC 
def app_start():
    while True:
        os.system("clear")
        view_menu = True
        menu()                                                                      # show the menu
        # initial assignment of lists
        people = list(AM.Load_People().values())
        drinks = list(AM.Load_Drinks().values())
        drinks_preferences = SL.LoadData().load_preferences('src/data/new_preferences.csv')    
        people_dic = AM.Load_People()
        print(people_dic)
        drinks_dic = AM.Load_Drinks()
        print(drinks_dic)
        while view_menu:                                                            # Loop for decision making, accounting for mistakes
            #try:    
                option = int(input("\nChoose your selection here (1-10): "))         # user picks their desired page
                if option == 1:
                    if len(people) == 0:
                        print("\nThere are no people present, add some!")
                    else:
                        table('PEOPLE', people)  
                    view_menu = False
                elif option == 2:
                    if len(drinks) == 0:
                        print("\nThere are no drinks, add some!")
                    else:
                        table('DRINKS', drinks) 
                    view_menu = False
                elif option == 3:
                    AM.add_person('PEOPLE')
                    view_menu = False
                elif option == 4:
                    AM.remove_person('PEOPLE', people)
                    view_menu = False
                elif option == 5:
                    AM.add_drink('DRINKS')
                    view_menu = False
                elif option == 6:
                    AM.remove_drink('DRINKS', drinks)
                    view_menu = False
                elif option == 7:
                    drinks_prefs = AM.assign_preference(people_dic, drinks_dic, people, drinks)
                    AM.preferences_display('PREFERENCES', drinks_prefs)
                    view_menu = False
                elif option == 8: 
                    preferences_table = AM.preferences_display("PREFERENCES", drinks_preferences)   
                    view_menu = False
                elif option == 9:
                    drinks_round = AC.Round(people, drinks)
                    beverages = drinks_round.order(people, drinks)
                    drinks_round.print_round(beverages)
                    view_menu = False
                elif option == 10:
                    print("\nThanks for stopping by, see you soon!\n")
                    exit()
                else: 
                    print("\nSorry I dont understand.\nPlease choose between 1 and 10.")
            # except ValueError as v:                                                             # Raised if anything other than an integer is input.
            #     print('\n')
            #     print(v)
            #     print("That is not an integer between 1 and 10, try again!")
            # except NameError as n:                                                              # Raised if the preferences list is opened without 
            #     print('\n')                                                                     # assigning people to drinks
            #     print(n)
                


        if not view_another_page():                                                             # Ending the app
            print("\nThanks for stopping by, see you soon!\n")  # FIX for 'if __name__ == "__main__"' clause!
            break 

if __name__ == "__main__":
    app_start()


# I made this on new-branch
# I AM ADDING A NEW PART TO BE COMMITTED