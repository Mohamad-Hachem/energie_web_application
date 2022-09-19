# let's import the needed files
from creating_database_connexion import mycol

# creating a query for with dpe being the search item
my_query = {'numero_dpe': '1401V1000455F'}

# searching in the database
results = mycol.find(my_query)

# printing the found results
for result in results:
    print(result)
