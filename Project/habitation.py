# importing the needed modules
from creating_database_connexion import mycol
import json
from useful_functions import query_creator
from typing import List
from typing import Dict


# let's create the function for retrieving all the documents needed
def search_all_habitation(length: int= 1, **kwargs):
    """This function takes nothing and returns all the documents"""

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

    # inserting in results the result of the query
    results = mycol.find(my_query)

    # since there is a lot we will take first 10 only
    count = 0
    result_list = []
    for result in results:
        # counting the number of things that we want in
        if count < length:
            # creating a temp dic to take the information needed
            temp_dict = {
                'maison': result['maison'],
                'quartier': result['quartier'],
                'batiment': result['batiment']
            }
            # transforming my dictionary into a json file then adding it to the list
            result_list.append(json.dumps(temp_dict))
            print(temp_dict)
        else:
            break
        count += 1

    # checking if the result is empty or not
    # if not empty simply return the results
    if len(result_list) != 0:
        return result_list
    # otherwise, return nothing found so the user can tell
    return "Nothing found"


# let's create the needed function
def search_habitation_by_ID(DPEID):
    """This function takes The dpe_ID and return the specific document"""

    # since it takes some time to finish the query we are going to put a sign to wait
    print("searching please wait...\n")

    # inserting the DPE_ID in the query
    my_query = {'numero_dpe': DPEID}

    # inserting in results the result of the query find_one()
    # find_one() is way better than find since it has a worst case scenario of O(n) whereas find() best case is O(n)
    results = mycol.find_one(my_query)

    if results is not None:
        # creating a temp dict
        temp_dict = {'maison': results['maison'], 'quartier': results['quartier'],
                     'batiment': results['batiment']}

        # transforming our dictionary into a json file
        temp_dict = json.dumps(temp_dict)

        # printing to see in pycharm
        print(temp_dict)

        # returning the results
        return temp_dict

    # if the results are none then
    return "Nothing found"
