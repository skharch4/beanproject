import database


MENU_PROMPT="""-- Coffee Bean App --

Please choose one of those options:

1)Add a new bean
2)Sell all beans
3)Find a bean by name:
4)See which preparation method is best for a bean.
5)Exit.

Your selection:"""


def menu():
    connection=database.connect()
    database.create_tables(connection)

    while(user_input := input(MENU_PROMPT)) !="5":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean_by_name(connection)
        elif user_input == "4":
            prompt_best_method(connection)
        else:
            print("Error! You must choose from 1 to 5")

def prompt_add_new_bean(connection):
    name = input("Enter name of your bean: ")
    method = input("Enter method of your bean: ")
    rating = int(input("Rate your bean on a scale of 1-100: "))

    database.add_bean(connection, name, method, rating)
def prompt_see_all_beans(connection):
    beans = database.get_all_beans(connection)
    for bean in beans:
        print(f" Name: {bean[1]} Method: {bean[2]} Rating:{bean[3]}/100")
def prompt_find_bean_by_name(connection):
    name = input("Print name of bean to find: ")
    beans = database.get_beans_name(connection, name)
    for bean in beans:
        print(f" Name: {bean[1]} Method: {bean[2]} Rating:{bean[3]}/100")
def prompt_best_method(connection):
    name = input("Print name of bean, for which you want to find method: ")
    best_method = database.get_best_preparation(connection, name)

    print(f"The best preparation method for {name} is: {best_method[2]}")
menu()