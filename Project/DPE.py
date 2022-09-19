# importing the needed modules
from creating_database_connexion import mycol
import json
from typing import List
from typing import Dict
from useful_functions import query_creator


# let's create the function for retrieving all the documents needed
def search_all_DPE(length:int= 1, **kwargs):
    """This function takes length and other variables and returns all the documents that meets the requirements"""

    # first we will create the right query by combining all the variable given in kwargs
    # then we will find the documents that satisfy our query
    # then we will print some documents depending on our length and needs of records

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

    # searching for the results in mongodb
    results = mycol.find(my_query)

    # printing the result and return the results
    count = 0
    result_list = []

    for result in results:
        if count < length:
            # deleting the '_id' from the row data, so we can use it as json
            del result['_id']
            # putting the result in our result list
            result_list.append(json.dumps(result))
        else:
            break
        count += 1

    # checking if the result is empty or not
    # if not empty simply return the results
    if len(result_list) != 0:
        print(result_list)
        return result_list
    # otherwise, return nothing found so the user can tell
    return "Nothing found"


# let's create the needed function
def search_DPE_by_ID(DPEID):
    """This function takes The dpe_ID and return the specific document"""

    # since it takes some time to finish the query we are going to put a sign to wait
    print("searching please wait...\n")

    # inserting the DPE_ID in the query
    my_query = {'numero_dpe': DPEID}

    # inserting in results the result of the query find_one()
    # find_one() is way better than find since it has a worst case scenario of O(n) whereas find() best case is O(n)
    results = mycol.find_one(my_query)

    if results is not None:

        # stripping away the '_id' that comes automatically from mongodb
        del results['_id']

        # transforming our dictionary into a json file
        json_result = json.dumps(results)

        # returning the results
        print(json_result)
        return json_result

    return "Nothing found"
