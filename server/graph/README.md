# GraphQL Structure
We are using GraphQL to grab specific data from our database. The database will be filled with renter information as well as the properties to coincide with each landlord.

Learn more about GraphQL here: https://graphql.org/

## The structure:
### schema:
Includes the schema of all the types of objects included in the database. This also has all the fields of data which can be queried from the object types.

### queries:
Includes definitions of each object type. The object types are broken down into return functions for each field that can be queried.

The query.py file returns the object types that can be queried.

### mutations.py
This file is used to define any fields within the defined objects types that we want to allow to be changed in the database. These changes could be things such as a price of a property going up or down, or a landlord changing their phone number.

### resolvers.py
The resolvers.py file combines everything from the mutations.py file, and all the files from the queries folder. This file is what our main app.py program interacts with.
