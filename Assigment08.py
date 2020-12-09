# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Paul Shaw,12.8.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    # #Constructor--#
    def __init__(self, product_name, product_value):
    # attributes#
        self.__product_name = str(product_name)
        self.__product_value = float(product_value)
    @property
    def product_name(self):
        return str(self.__product_name)
    @product_name.setter
    def product_name(self, name):
        if str(name).isnumeric():
            self.__product_name = name
        else:
            raise Exception("Product name must not be a number")
    @property
    def product_value(self):
        return float(self.__product_value)
    @product_value.setter
    def product_value(self, value):
        if str(value).isnumeric():
            self.__product_value = value
        else:
            raise Exception("Product value must be a number")
    #Methods
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + "," + str(self.product_value)


"""Stores data about a product:

    properties:"""
   # @property
   # def product_name(self)
"""product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:"""

    #"""changelog: (When,Who,What)
        #RRoot,1.1.2030,Created Class
       # <Your Name>,<Today's Date>,Modified code to complete assignment 8"""
    #"""
   # pass
    # TODO: Add Code to the Product class
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)"""
    @staticmethod
    def read_data_from_file(file_name):
        list_of_prod_rows = []
        fileopen = open(file_name, "r")
        for line in fileopen:
            data = line.split(",")
            row = Product(data[0],data[1])
            list_of_prod_rows.append(row)
        fileopen.close()
        return list_of_prod_rows
    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        filesave = open(file_name, "w")
        for product in list_of_rows:
            filesave.write(product.__str__() + "\n")
        filesave.close()
        print("Products saved to file")
    """changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #"""
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing"
        """
        print('''
        Menu of Options
        1) Show current product list
        2) Add new product to list
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        StrChoice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return StrChoice

    @staticmethod
    def print_current_Products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products in the system are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_value) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_value():
        strproduct = str(input("Enter a new product:  ")).strip() #user input for task
        fltvalue = float(input("Enter the value: ")) #user input for priority
        print()
        prod = Product(product_name=strproduct, product_value=fltvalue)
        print("Product Added")
        return prod



    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user"""
"""Print("Mega-Store USA Inventory List")
f = FileProcessor()
print(f.read_data_from_file("products.txt"))"""
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from products.txt.
#FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

# Step 2 - Display a menu of choices to the user
lstOfProductObjects =FileProcessor.read_data_from_file(strFileName)
while(True):
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    if strChoice.strip() == '1':# Step 3 Show current data
        IO.print_current_Products_in_list(lstOfProductObjects)  # Show current data in the list/table
        IO.print_menu_Tasks()  # Shows menu
        strChoice = IO.input_menu_choice()  # Get menu option
        continue
    # Step 4 - Process user's menu choice
    elif strChoice.strip() == '2':  # Add a new Product
        lstOfProductObjects.append(IO.input_new_product_and_value())
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
            print("data saved!")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break   # and Exit
