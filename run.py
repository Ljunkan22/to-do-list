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
    hej
    """
    option = 1

    options_selector(option)


def options_selector(option):
    """
    hej
    """

    list_of_functions = [function0, function1, function2]
    list_of_functions[option]()


def function0():
    """
    hej
    """
    print("function 0")


def function1():
    """
    hej
    """
    print("function 1")


def function2():
    """
    hej
    """
    print("function 2")
