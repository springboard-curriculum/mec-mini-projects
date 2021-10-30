from sqlite3.dbapi2 import connect
import pandas as pd
import json
import sqlite3

#connect to an sql database
#for modularity have function take the name of a database, but for now
#focus on the point of converting json to sql using python
database = "../example.sqlite"
conn = sqlite3.connect(database)

#open the json file for reading
#load the json file into a container
#convert the json file to a dataframe

'''again for future thought: function would take parameter for filename,
add error checking to make sure file is a json file
add error checking for format of file
use json_normalize to break list of dicts into key:values pairs to column:row.values
'''
#convert df to sql using connection from def connect_to_sql
with open ('author.json','r') as f:
    jsondata = json.loads(f.read())

df = pd.json_normalize(jsondata)
print(df)

df.to_sql(name='Authors', con=conn)
conn.close()
