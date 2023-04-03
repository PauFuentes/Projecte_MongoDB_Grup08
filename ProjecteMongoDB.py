from pymongo import MongoClient

# establecer la conexión
Host = 'localhost' # localhost per connexions a la màquina main
Port = 27017
client = MongoClient("mongodb://{}:{}".format(Host,Port))

# elegir la base de datos
db = client['Sessio9_def']

if 'comtrade_def' in db.list_collection_names():
    coll = db['comtrade_def']
    coll.drop()

coll = db.create_collection('comtrade_def')

# elegir la colección
collection = db['comtrade_def']

import pandas as pd

# leer el archivo CSV
df = pd.read_csv('comtrade2.csv')

# convertir el dataframe a una lista de diccionarios
data = df.to_dict('records')

print(data)
# insertar los documentos en la colección
collection.insert_many(data)