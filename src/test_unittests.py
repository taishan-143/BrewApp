import unittest
from unittest.mock import Mock, patch 
from app_methods import *
from app_classes import *
from table_function import *

# class Test_Methods(unittest.TestCase):

#  # First 5 require input from user to test, fix this!
    
#     def test_table_width(self):
#         # Arrange
#         header = 'TEST'
#         data = ['Test line 1', 'Test line 2', 'Test line 3']
#         expected = 17     # accounting for the length of enumerate value and empty spaces
#         # Act
#         actual = table_width(header, data)
#         # Assert
#         try:
#             assert expected == actual
#             print("\nTEST SUCCESS")
#         except Exception:
#             print("\nTEST FAILURE")

#     def test_table(self):
#         # Arrange 
#         pass
#         # Act

#         # Assert


#     def test_preferences_display(self):
#         # Arrange
#         header = 'TEST'
#         data = {'John':'Beer', 'Alex':'Cider'}
#         expected = """
#         +===================================+
#         | TEST                              |
#         +===================================+
#         | [1] John's favourite drink: Beer  |
#         | [2] Alex's favourite drink: Cider |
#         +===================================+
#         """
#         # Act
#         actual = preferences_display(header, data)
#         # Assert
#         try:
#             assert expected == actual
#             print("\nTEST SUCCESS")
#         except Exception:
#             print("\nPREFS DISPLAY -- TEST FAILED")      # CURRENTLY FAILING


class Test_Assign_Preference(unittest.TestCase):
    
    
    @patch("builtins.input")
    def test_assign_preference_inputs(self, mock_input):
        # Arrange
        mock_Preferences = Mock(Preferences)
        people = ['Taishan', 'John', 'Matt']
        drinks = ['Mai Tai', 'Stella', 'Mahou']
        mock_input.side_effect = [1, 1,'n']
        expected = {'Taishan':'Mai Tai'}
        # Act
        actual = assign_preference(people, drinks)
        # Assert
        try:
            self.assertEqual(expected, actual)
            print("\nassign_preference test --> SUCCESS")
        except Exception:
            print('\nassign_preference test --> FAILURE!')


class Test_Preferences_Class(unittest.TestCase):

    @patch("app_classes.Preferences.data_dictionary")
    def test_data_dictionary(self, mock_data_dictionary):
        # Arrange
        preferences = Mock(Preferences)
        data = ['Name 1', 'Name 2', 'Name 3']
        mock_data_dictionary = {1:'Name 1', 2:'Name 2', 3:'Name 3'} 
        # Act
        actual = Preferences().data_dictionary(data)
        # Assert
        try:
            self.assertEqual(mock_data_dictionary, actual)
            print("\nPreferences().data_dictionary test --> SUCCESS")
        except:
            print("\nPreferences().data_dictionary test --> FAILURE!")


    @patch("app_classes.Preferences.choose_name")
    @patch("builtins.input")
    def test_choose_name(self, mock_input, mock_choose_name):
       # Arrange
        preferences = Mock(Preferences)
        data_dic = {1:'Taishan', 2:'Jack'}
        selected_name = []
        people = ['Taishan', 'Jack']
        mock_input.return_value = 1
        mock_choose_name = 'Taishan'
        # Act
        actual =  Preferences().choose_name(data_dic, selected_name, people)
        # Assert
        try:
            self.assertEqual(mock_choose_name, actual)
            print("\nPreferences().choose_name test --> SUCCESS")
        except:
            print("\nPreferences().choose_name test --> FAILURE!")

    @patch("app_classes.Preferences.choose_drink")
    @patch("builtins.input")
    def test_choose_drink(self, mock_input, mock_choose_drink):
        # Arrange 
        preferences = Mock(Preferences)
        data_dic = {1:'Mahou', 2:'Stella'}
        drinks = ['Mahou', 'Stella']
        mock_input.return_value = 1
        mock_choose_drink = 'Mahou'
        # Act 
        actual = Preferences().choose_drink(data_dic, drinks)
        # Assert
        try:
            self.assertEqual(mock_choose_drink, actual)
            print("\nPreferences().choose_drink test --> SUCCESS")
        except:
            print("\nPreferences().choose_drink test --> FAILURE")

    @patch("builtins.input")
    def test_add_another(self, mock_input):
        # Arrange
        preferences = Mock(Preferences)
        mock_input.return_value = 'n'
        # Act
        actual = Preferences().add_another()
        # Assert
        try:
            self.assertFalse(actual)
            print("\nPreferences().add_another test --> SUCCESS")
        except:
            print("\nPreferences().add_another test --> FAILURE")

class Test_Add_To_Table(unittest.TestCase):
    
    @patch("builtins.input")
    def test_all_inputs_from_add_to_table_function(self, mock_input):
        # Arrange
        add_to_table_mock = Mock(add_to_table)
        add_to_table_mock.header = 'DRINKS'
        add_to_table_mock.data = ['Stella', 'Mahou']
        mock_input.side_effect = ['Mojito', 'n', None]
        expected = ['Stella', 'Mahou', 'Mojito']
        # Act
        actual = add_to_table(add_to_table_mock.header, add_to_table_mock.data)
        print(actual)
        # Assert
        try:
            self.assertEqual(expected, actual)
            print("Add to table test --> SUCCESS")
        except Exception:
            print("Add to table test --> FAILURE")

class Test_Remove_From_Table(unittest.TestCase):

    @patch("builtins.input")
    def test_all_inputs_in_remove_from_table_function(self, mock_input):
        # Arrange
        remove_from_table_mock = Mock(remove_from_table)
        remove_from_table_mock.header = 'DRINKS'
        remove_from_table_mock.data = {1:'Stella', 2:'Mahou', 3:'Mojito'}
        mock_input.side_effect = [3, 'n', None]
        expected = {1:'Stella', 2:'Mahou'}
        # Act 
        actual = remove_from_table(remove_from_table_mock.header, remove_from_table_mock.data)
        # Assert
        try:
            self.assertEqual(expected, actual)
            print("Remove from table test --> SUCCESS")
        except Exception:
            print("Remove from table test --> FAILURE")
    

if __name__ == "__main__":
    unittest.main()