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
        "4: Display items that are not done\n"
        "5: Remove the entire list\n"
        )

    try:
        option = int(input("Enter your number here:\n "))

        if 1 <= option <= 5:
            print(LINE)
            options_selector(option)

        raise ValueError()
    except ValueError:
        print(LINE)
        print("Your number is not between 1-5,")
        print("please try again \n")
        get_option()


def display_list(column1, column2, column3):
    """
    Get the list from the worksheet and displays it
    """
    print("this is on your to do list \n")
    i = 1
    while i < len(column1):
        print(
            f"{i} {column1[i]} Takes about {column2[i]} min {column3[i]} \n"
            )
        i += 1

    return_to_main()


def check_of_items(column1, column2, column3):
    """
    Update the worksheet to mark items as done
    """
    print("this is on your to do list \n")
    i = 1
    while i < len(column1):
        print(
            i, column1[i], "Takes about " +
            column2[i] + " minutes " + column3[i] + "\n")
        i += 1
    items = SHEET.worksheet("list_one").get_all_values()
    print("What item are you done with")
    print("input the number corresponding to the item")
    print("If you want to return to main menu input 0")

    try:
        option = int(input("Enter your number here:\n "))

        if option == 0:
            get_option()

        if option < len(column3):
            items[option][2] = "Done"
            SHEET.worksheet("list_one").update(items)
            check_of_items(column1, column2, column3)

        raise ValueError()
    except ValueError:
        print(LINE)
        print("Your entry was not a valid number!")
        print("You need to enter a number corresponding to an item")
        print("please try again \n")
        check_of_items(column1, column2, column3)


def add_item():
    """
    Adds one or more items to the list
    """
    print("Enter a new item to the list")
    print("Example: Go for a run")
    print("If you want to return to main menu input 0\n")

    try:
        new_item = input("Enter your item here:\n ")

        if new_item == "0":
            print(LINE)
            get_option()

        if new_item == "":
            print(LINE)
            print("Yor entry cant be blank")
            print("please try again \n")
            add_item()

        print(LINE)
        print("Enter how long you think it's going to take in minutes")
        print("Example: 45\n")
        new_time = int(input("Enter the time here:\n "))

        if new_time == 0:
            get_option()

        new_row = [new_item, str(new_time), "Not done"]
        SHEET.worksheet("list_one").append_row(new_row)
        print(LINE)
        add_item()

        raise ValueError()
    except ValueError:
        print(LINE)
        print("That is not a valid number!\n")
        print("please try again \n")
        add_item()


def display_items_left(column1, column2, column3):
    """
    Displays items that are not markt as done
    """
    time_sum = 0
    i = 1
    while i < len(column3):
        if column3[i] == "Not done":
            print(
                f"{i} {column1[i]} Takes about {column2[i]}"
                f" min {column3[i]} \n")

            time_sum += int(column2[i])

        i += 1
    hour_sum = time_sum / 60
    min_sum = round(0 + (hour_sum - int(hour_sum)) * 60)
    print(f"It will take you aboute {time_sum} min to get all the items done")
    print(f"Or about {int(hour_sum)} hours and {min_sum} min\n")
    print(LINE)

    return_to_main()


def remove_all_items():
    """
    hej
    """
    print("Do you want to remove all the items in the list?")
    print("Enter 0 to return to manin page or 1 to remove the list\n")

    try:
        remove_list = int(input("Enter answer here:\n"))

        if remove_list == 0:
            print(LINE)
            get_option()

        if remove_list == 1:
            SHEET.worksheet("list_one").clear()

            header = ["Thing to do", "Time", "Status"]
            SHEET.worksheet("list_one").append_row(header)

            print(LINE)
            get_option()

        raise ValueError()
    except ValueError:
        print(LINE)
        print("Entry was not valid")
        print("please try again \n")
        remove_all_items()


def return_to_main():
    """
    returns the user to main menu if 0 is inputed
    """
    print("input 0 to return to main menu")

    try:
        input0 = int(input("Enter 0 here:\n "))

        if input0 == 0:
            print(LINE)
            get_option()

        raise ValueError()
    except ValueError:
        print(LINE)
        print("Your number is not 0!")
        print("please try again \n")
        return_to_main()


def options_selector(option):
    """
    Use the number inputed and runs the corresponding funtion
    and gets the values from worksheet
    """

    items = SHEET.worksheet("list_one").get_all_values()
    column1 = [item[0] for item in items]
    column2 = [item[1] for item in items]
    column3 = [item[2] for item in items]

    list_of_functions = [
        get_option, display_list, check_of_items, add_item,
        display_items_left, remove_all_items
        ]

    if option in (3, 5):
        list_of_functions[option]()

    list_of_functions[option](column1, column2, column3)


get_option()
