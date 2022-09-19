# importing the needed modules
from creating_database_connexion import mycol
from typing import List
from typing import Dict
from useful_functions import query_creator


# creating a function that count certain things
def inventory_count(**kwargs):
    """This function takes length and other variables and returns all the documents that meets the requirements"""

    # first we will create the right query by combining all the variable given in kwargs
    # then we will find the documents that satisfy our query
    # then we will print some documents depending on our length and needs of records
    print(kwargs)
    # start by creating a list that will hold our needed conditions
    query_list: List[Dict] = []

    # a function that takes all the kwargs and create the right query for us
    query_creator(query_list, **kwargs)

    # finalizing the query that we will pass to mongodb
    # if there is conditions then the query is created in this form
    if len(query_list):
        my_query = {"$and": query_list}
    # if it is empty this means the user doesn't specific details only raw materials
    else:
        my_query = {}

    # since it takes some time to finish the query we are going to put a sign to wait
    print("searching please wait...\n")

    # TRYING... 649469 1.50min
    return mycol.count_documents(my_query)
