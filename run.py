import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('to_do_list')


def get_option():
    """
    Gets what funtion the user wants to run
    and gets the items from worksheet
    """
    print("welcome to your To Do List\n")
    print("Input the number corresponding to the function you want\n")
    print(
        "1: Display your to do list\n"
        "2\n"
        "3\n"
        "4\n"
        "5\n"
        )

    option = int(input("Enter your data here:\n "))

    if option > 6:
        print(f"Your number is not between 1-5, you provided {option}!")
        print("please try again \n")
        get_option()
    else:
        options_selector(option)


def display_list():
    """
    Get the list from the worksheet and displays it
    """
    items = SHEET.worksheet("list_one").get_all_values()

    column1 = [item[0] for item in items]
    column2 = [item[1] for item in items]

    print("this is on your to do list \n")
    i = 0
    while i < len(column1):
        print(column1[i], "This will take about " + column2[i] + " minutes\n")
        i += 1

    return_to_main()


def check_of_items():
    """
    hej
    """
    print("check_of_items")


def add_item():
    """
    hej
    """
    print("add_item")


def display_items_left():
    """
    hej
    """
    print("display_items_left")


def remove_all_items():
    """
    hej
    """
    print("remove_all_items")


def return_to_main():
    """
    returns the user to main menu if 0 is inputed
    """
    print("input 0 to return to main menu")

    input0 = int(input("Enter your data here:\n "))

    if exit == 0:
        print(f"Your number is not 0, you provided {input0}!")
        print("please try again \n")
        return_to_main()
    else:
        get_option()


def options_selector(option):
    """
    Use the number inputed and runs the corresponding funtion
    """

    list_of_functions = [
        get_option, display_list, check_of_items, add_item,
        display_items_left, remove_all_items
        ]
    list_of_functions[option]()


get_option()
