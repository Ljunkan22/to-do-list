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
    print("Input what function you want to run\n")
    print("You input should be a number between 1-5 the number corresponds to different functions\n")
    print(
        "1\n"
        "2\n"
        "3\n"
        "4\n"
        "5\n"
        )

    option = input.int("Enter your data here:\n ")

    options_selector(option)


def options_selector(option):
    """
    hej
    """

    list_of_functions = [
        get_option, display_items1, check_of_items, add_item,
        display_items_left, remove_all_items
        ]
    list_of_functions[option]()


def display_items1():
    """
    hej
    """
    print("display_items")


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


get_option()
