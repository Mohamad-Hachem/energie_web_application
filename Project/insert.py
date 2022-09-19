# let's import our needed modules
import json
import pymongo
from creating_database_connexion import mycol


# the following code will allow us to go to the records file and import the records into the needed database
# there is 96 json files

# We will do this in batches because it would be easier on Microsoft Azure
option1 = input('Press 1 if you want things to work in 1 press Press 2 for batches\n')

if option1 == '1':
    for i in range(0, 96):

        # starting with opening the json files
        with open(f"./records/record{i}.json") as file:

            # loading the json files
            print(f"we are loading file {i} out of 96 still {96 - i} remaining")
            file_data = json.load(file)

            # transform them into a list of dictionaries to be able to put it in mongodb
            print(f"we are appeding this patch  {i} out of 96 still {96 - i} remaining")
            final_data = []
            for item_file in file_data:
                final_data.append(item_file)

            # inserting the data into mongodb
            print(f"we are inserting {i} out of 96 still {96 - i} remaining")
            mycol.insert_many(final_data)

else:

    option = input('Enter the number of the batch there is 5 batches do them one by one\n')
    option = int(option)

    for i in range((option-1)*20, option*20):

        # records are 0 to 95
        if i == 96 :
            break

        # starting with opening the json files
        with open(f"./records/record{i}.json") as file:

            # loading the json files
            print(f"we are loading file {i} out of 96 still {96-i} remaining")
            file_data = json.load(file)

            # transform them into a list of dictionaries to be able to put it in mongodb
            print(f"we are appeding this patch  {i} out of 96 still {96-i} remaining")
            final_data = []
            for item_file in file_data:
                final_data.append(item_file)

            # inserting the data into mongodb
            print(f"we are inserting {i} out of 96 still {96-i} remaining")
            mycol.insert_many(final_data)
    print(f'We have finished batch number {option} there is {option-5} left')