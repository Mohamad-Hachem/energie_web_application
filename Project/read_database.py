# importing the needed modules
from creating_database_connexion import mycol


# printing the records that we have
def print_all():
    """This function takes nothing and return all the 9M records in mangodb"""
    for x in mycol.find():
        print(x)


# printing the first element that we have
def print_head():
    """This function takes nothing and returns the first element of our mangodb database"""
    print("================================")
    print(mycol.find().next())
    print("================================")


# print the first 10 elements that we have
def print_certain_amount(amount: int):
    """This function will return the first 10 elements in the database"""
    counter = 0
    for x in mycol.find():
        if counter < amount:
            print("================================")
            print(x)
            counter += 1
        else:
            break
    print("================================")


# giving the user the possibility to explore the records
option = ""
while option != "Q":

    # Asking the user what he would like to give
    option = input("PLease insert the corresponding letter to get the needed results:\n"
                   "Insert F to get 1 record\n"
                   "Insert any number to get that much records\n"
                   "Insert A to get All records ( TAKES 2 HOURS TO FINISH )"
                   "Insert Q to exit\n")

    # putting option to lower case so we can deal with it without any issue if the user uses capital
    option = option.lower()

    # according to what the use chooses we can see the results
    if option == "f":
        print_head()
    elif option == "a":
        print_all()
    elif option == "Q":
        pass
    else:
        print_certain_amount(int(option))
