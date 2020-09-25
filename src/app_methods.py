from app_classes import * 
from table_function import table, table_width 

def add_to_table(header, data):
    add_more = True
    add_new = True
    while add_new:
        # checks for people or drinks
        if header == "DRINKS":
            item = 'drink'
        else:
            item = 'person'
        # ask user for data input 
        new_data = input(f"\nPlease add a new {item} to the list: ").title()
        # CHECK FOR REPEAT NAMES
        # append input to the data list
        data.append(new_data)
        # ask user again whether they want to input more
        while add_more:
            choice = input(f"Do you want to add more {header.lower()}, Y or N?: ")
            if choice == '':
                continue
            
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

def remove_from_table(header, data):
    # check if people or drinks being removed
    not_removed_item = True
    while not_removed_item:
        if header == 'DRINKS':
            item = 'drink'
        else:
            item = 'person'
    # ask user to input a number to remove an item
        not_chosen_item = True
        while not_chosen_item:
            try:
                data_pop = int(input(f"\nChoose a {item} to remove (1-{len(data.keys())}): "))
                if data_pop not in data.keys():
                    print("You're out of range! Try again.")
                    not_chosen_item = True
                elif data_pop in data.keys():
                    not_chosen_item = False
                else:
                    print("Sorry, I don't understand.")
                    not_chosen_item = True
            except Exception as e:
                print("Sorry, I don't Understand")
        # CHECK FOR REPEAT REMOVAL!
        data.pop(data_pop)

        remove_another = True
        while remove_another:
            choice = input(f"Would you like to remove another {item}, Y or N?: ")
            if choice == '':                                                            # check for no input
                continue
            if choice[0] == 'N' or choice[0] == 'n':
                print("\nThank you!")
                remove_another = False
                not_removed_item = False
            elif choice[0] == 'Y' or choice[0] == 'y':
                remove_another = False
                not_removed_item = True
            else:
                print("\nSorry, I dont understand!")

    return data      # dictionary to be sorted into a list of values in the main app.

def assign_preference(people, drinks): 
    selected_name = []                                                              # list to check no multiple assignments occur 
    preferences_dictionary = {}
    not_chosen_preference = True
    while not_chosen_preference:
        new_preference = Preferences()                                           # instantiate preference class
        people_dic = new_preference.data_dictionary(people)                         # create people dictionary
        drinks_dic = new_preference.data_dictionary(drinks)                         # create drinks dictionary   
        Name = new_preference.choose_name(people_dic, selected_name, people)        # get a person from the names file
        Drink = new_preference.choose_drink(drinks_dic, drinks)                     # get a drink from the drinks file
        not_chosen_preference = new_preference.add_another()
                                                                                    
        chosen_name = True
        chosen_drink = True
        selected_name.append(Name)
        preferences_dictionary[f'{Name}'] = f'{Drink}'
    
    return preferences_dictionary

# To solve overwriting issue:
# Append to pre-existing preferences dictionary
# delete repeat values. 

def preferences_display(header, data):                           
    items = [] 
    [items.append(f"{name}'s favourite drink: {data[name]}") for name in data.keys()]
    table(header, items)

