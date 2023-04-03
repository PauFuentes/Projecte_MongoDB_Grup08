from pymongo import MongoClient

# establecer la conexión
Host = 'dcccluster.uab.es' # localhost per connexions a la màquina main
Port = 8222
client = MongoClient("mongodb://{}:{}".format(Host,Port))

# elegir la base de datos
db = client['Comics']

if 'Editorial' in db.list_collection_names():
    coll = db['Editorial']
    coll.drop()

coll = db.create_collection('Editorial')

if 'Colleccio' in db.list_collection_names():
    coll = db['Colleccio']
    coll.drop()

coll = db.create_collection('Colleccio')

if 'Publicacio' in db.list_collection_names():
    coll = db['Publicacio']
    coll.drop()

coll = db.create_collection('Publicacio')

if 'Artista' in db.list_collection_names():
    coll = db['Artista']
    coll.drop()

coll = db.create_collection('Artista')

if 'Personatge' in db.list_collection_names():
    coll = db['Personatge']
    coll.drop()

coll = db.create_collection('Personatge')

# elegir la colección
import pandas as pd

# leer el archivo CSV
xls = pd.ExcelFile('Dades (1).xlsx')
Editorial = pd.read_excel(xls,'Colleccions-Publicacions', usecols=[0,1,2,3])
Colleccio = pd.read_excel(xls,'Colleccions-Publicacions', usecols=[4,5,6,7,8,9,10,11,12,13,14])
Publicacio = pd.read_excel(xls,'Colleccions-Publicacions', usecols=[15,16,17,18,19,20,21,22,23,24])
Personatges = pd.read_excel(xls,'Personatges')
Artistes = pd.read_excel(xls,'Artistes')

# convertir el dataframe a una lista de diccionarios
Editorial = Editorial.to_dict('records')
Colleccio = Colleccio.to_dict('records')
Publicacio = Publicacio.to_dict('records')
Personatges = Personatges.to_dict('records')
Artistes = Artistes.to_dict('records')
print(Editorial)
print(Colleccio)
print(Publicacio)
print(Personatges)
print(Artistes)
# insertar los documentos en la colección
collection = db['Editorial']

#collection.insert_many(data1)