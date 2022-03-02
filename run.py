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

LINE = "_________________________________________________________________\n"


def get_option():
    """
    Gets what funtion the user wants to run
    and gets the items from worksheet
    """
    print("welcome to your To Do List\n")
    print("Input the number corresponding to the function you want\n")
    print(
        "1: Display your to do list\n"
        "2: Check of items\n"
        "3: Add items to list\n"
        "4\n"
        "5\n"
        )

    option = int(input("Enter your number here:\n "))
    print()
    if option >= 5:
        print(f"Your number is not between 1-5, you provided {option}!")
        print("please try again \n")
        get_option()
    else:
        print(LINE)
        options_selector(option)


def display_list():
    """
    Get the list from the worksheet and displays it
    """
    items = SHEET.worksheet("list_one").get_all_values()

    column1 = [item[0] for item in items]
    column2 = [item[1] for item in items]
    column3 = [item[2] for item in items]

    print("this is on your to do list \n")
    i = 1
    while i < len(column1):
        print(
            f"{i} {column1[i]} Takes about {column2[i]} min {column3[i]} \n"
            )
        i += 1

    return_to_main()


def check_of_items():
    """
    Update the worksheet to mark items as done
    """
    items = SHEET.worksheet("list_one").get_all_values()

    column1 = [item[0] for item in items]
    column2 = [item[1] for item in items]
    column3 = [item[2] for item in items]

    print("this is on your to do list \n")
    i = 1
    while i < len(column1):
        print(
            i, column1[i], "Takes about " +
            column2[i] + " minutes " + column3[i] + "\n")
        i += 1

    print("What item are you done with")
    print("input the number corresponding to the item")
    print("If you want to return to main menu input 0")

    option = int(input("Enter your number here:\n "))

    if option == 0:
        get_option()

    if option < len(column3):
        items[option][2] = "Done"
        SHEET.worksheet("list_one").update(items)
        check_of_items()
    else:
        print(str(option), " is not a valid number!")
        print("Number must be between 0 and", str(len(column1)-1))
        check_of_items()


def add_item():
    """
    Adds one or more items to the list
    """
    print("If you want to return to main menu input 0\n")

    print("Input a new item to the list")
    print("Example: Go for a run\n")
    new_item = input("Enter your item here:\n ")

    if new_item == "0":
        print(LINE)
        get_option()

    try:
        print("Input how long you think it's going to take in minutes")
        print("Example: 45\n")
        new_time = int(input("Enter the time here:\n "))

        if new_time == 0:
            get_option()

    except ValueError:
        print(LINE)
        print("This is not a valid number!\n")
        add_item()

    new_row = [new_item, str(new_time), "Not done"]
    SHEET.worksheet("list_one").append_row(new_row)

    print(LINE)
    add_item()


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
    print(LINE)
    print("input 0 to return to main menu")

    input0 = int(input("Enter your data here:\n "))

    if input0 == 0:
        get_option()
    else:
        print(f"Your number is not 0, you provided {input0}!")
        print("please try again \n")
        return_to_main()


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
