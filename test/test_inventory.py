# importing needed modules
from Project.inventory import inventory_count

# TODO: In the inventory we have only one functinality and we are going to test it


# This test is probably not necessary since we are testing directly some mongodb functionality
# creating a test for inventory
def test_inventory_count(fake_kwargs_inventory):
    """This is a test to test the inventory functionality"""

    # act part
    responses = inventory_count(**fake_kwargs_inventory)

    # assert part
    assert 2651 == responses
