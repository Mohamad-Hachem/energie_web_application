# importing needed modules
from Project.useful_functions import key_transform, query_creator
import pytest


# testing if the key_transform function works as we want
@pytest.mark.parametrize("keys, expected_responses", [
    ("classe_consommation_energie", "consommations_energie.classe_consommation_energie"),
    ("consommation_energie", "consommations_energie.consommation_energie"),
    ("nom_methode_dpe", "methodologie.nom_methode_dpe")
])
def test_key_transform(keys, expected_responses):
    """This test takes keys and assert that should be equal to the expected responses"""

    # act part of the test
    responses = key_transform(keys)

    # assert part
    assert expected_responses == responses


# testing if the query_creator function works as we want
def test_query_creator(fake_query_list, fake_kwargs):
    """This is a test to test the query_creator function"""

    # this is the arrange part
    # creating an empty list that we will run it through query_creator function
    # then compare it with our pre-made fake_query_list
    testing_query = []

    # this is the act part where we take the testing_query and change it according to
    # query_creator function
    query_creator(testing_query, **fake_kwargs)

    # this is the assert part where we check if testing_query is equal to fake_query_list
    assert fake_query_list == testing_query
