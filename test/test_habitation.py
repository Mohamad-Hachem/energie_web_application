# importing needed modules
from unittest import mock
from test.mock import EXPECTED_VALUES_MOCK_FIND_ALL_HABITATION, EXPECTED_VALUES_MOCK_FIND_ONE
from Project.habitation import search_all_habitation, search_habitation_by_ID

# TODO: 1-There is 2 possibility for search_all_habitation(found or not) therefor we have 2 tests


# First test if we found the information
# creating a test to check if search_all_DPE working well
@mock.patch('Project.habitation.mycol.find')
def test_search_all_habitation_found(mock_mycol_find, expected_results_search_all_habitation, fake_kwargs_habitation):
    """This is a function to test if search_all_dpe is working as it should"""

    # arrange part of the test
    mock_mycol_find.return_value = EXPECTED_VALUES_MOCK_FIND_ALL_HABITATION

    # act part of the test
    responses = search_all_habitation(1, **fake_kwargs_habitation)

    # assert part of the test
    assert expected_results_search_all_habitation == responses

    # asserting the mock working and called only one time
    mock_mycol_find.assert_called_once()


# Second test if the information is not found
# creating a test to check if search_all_DPE working well
@mock.patch('Project.habitation.mycol.find')
def test_search_all_habitation_not_found(mock_mycol_find, fake_kwargs_habitation):
    """This is a function to test if search_all_dpe is working as it should"""

    # arrange part of the test
    mock_mycol_find.return_value = []

    # act part of the test
    responses = search_all_habitation(1, **fake_kwargs_habitation)

    # assert part of the test
    assert "Nothing found" == responses

    # asserting the mock working and called only one time
    mock_mycol_find.assert_called_once()


# TODO: 2-There is 2 possibility for search_all_habitation_by_id (found or not) therefor we have 2 tests
# first Test if we found the information
# creating a test to check if search_all_habitation_by_id
@mock.patch('Project.DPE.mycol.find_one')
def test_search_all_dpe_by_id_found(mock_find_one, fake_id, expected_results_search_habitation_dpe_by_id):
    """This test tests if search_all_habitation_by_id works as it should"""

    # arrange part of the test ( mocking find_one so we eliminate outside issues)
    mock_find_one.return_value = EXPECTED_VALUES_MOCK_FIND_ONE

    # act part of the test
    responses = search_habitation_by_ID(fake_id)

    # assert part of the test
    assert expected_results_search_habitation_dpe_by_id == responses

    # asserting the mock was called only once
    mock_find_one.assert_called_once()


# Second Test if the information can't be found
# creating a test to check if search_all_habitation_by_id
@mock.patch('Project.DPE.mycol.find_one')
def test_search_all_dpe_by_id_not_found(mock_find_one, fake_id):
    """This test tests if search_all_habitation_by_id works as it should"""

    # arrange part of the test ( mocking find_one so we eliminate outside issues)
    mock_find_one.return_value = None

    # act part of the test
    responses = search_habitation_by_ID(fake_id)

    # assert part of the test
    assert "Nothing found" == responses

    # asserting the mock was called only once
    mock_find_one.assert_called_once()
