# importing needed modules
from typing import List
from typing import Dict


# creating a function to transform key to the right words
def key_transform(key: str) -> str:
    """This function takes a string and returns the right string for the query"""

    if key == "classe_consommation_energie":
        return "consommations_energie.classe_consommation_energie"

    if key == "consommation_energie":
        return "consommations_energie.consommation_energie"

    if key == "nom_methode_dpe":
        return "methodologie.nom_methode_dpe"

    if key == "classe_estimation_ges":
        return "emissions_ges.classe_estimation_ges"

    if key == "secteur_activite":
        return "batiment.secteur_activite"

    if key == "surface_habitable":
        return "maison.surface_habitable"

    if key == "annee_construction":
        return "batiment.annee_construction"

    if key == "DPE":
        return "numero_dpe"


def query_creator(query_list: List[Dict], **kwargs):
    # trying to see if we can pass the arguments as kwargs
    for key, value in kwargs.items():

        # making sure to receive the right key
        key = key_transform(key)

        # creating the temp dict that will be passed to the query
        if key == 'consommations_energie.consommation_energie' or key == "maison.surface_habitable":

            # if key is one of these 2 than we are receiving a certain format; therefore, we split
            value = value.split("-")
            # putting the query in a temp dict
            temp_dict = {"$and": [{key: {"$gt": int(value[0])}}, {key: {"$lt": int(value[1])}}]}

        else:
            # putting the query in a temp dict
            temp_dict = {key: value}

        # adding the temp_dict the list of queries that will be passed on
        query_list.append(temp_dict)
