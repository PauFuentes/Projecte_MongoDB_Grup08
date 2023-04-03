from pymongo import MongoClient
import pprint

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
Editorial = pd.read_excel(xls,'Editorial')
Colleccio = pd.read_excel(xls,'Colleccions')
Publicacio = pd.read_excel(xls,'Publicacions')
Personatges = pd.read_excel(xls,'Personatges')
Artistes = pd.read_excel(xls,'Artistes')

# convertir el dataframe a una lista de diccionarios
Editorial = Editorial.to_dict('records')
Colleccio = Colleccio.to_dict('records')
Publicacio = Publicacio.to_dict('records')
Personatges = Personatges.to_dict('records')
Artistes = Artistes.to_dict('records')

for col in Colleccio:
    col['genere'] = col['genere'].strip('][').split(', ')
    col['ISBN_publicacions'] = col['ISBN_publicacions'].strip('][').split(',')
    col['titol_publicacions'] = col['titol_publicacions'].strip('][').split(',')

for pub in Publicacio:
    pub['guionistes'] = pub['guionistes'].strip('][').split(',')
    pub['dibuixants'] = pub['dibuixants'].strip('][').split(', ')
    pub['id_dibuixants'] = pub['id_dibuixants'].strip('][').split(',')
    pub['id_guionistes'] = pub['id_guionistes'].strip('][').split(',')

for per in Personatges:
    per['guionistes'] = per['guionistes'].strip('][').split(',')
    per['dibuixants'] = per['dibuixants'].strip('][').split(', ')
    per['id_dibuixants'] = per['id_dibuixants'].strip('][').split(',')
    per['id_guionistes'] = per['id_guionistes'].strip('][').split(',')
"""
print(Editorial)
print(Colleccio)
print(Publicacio)
print(Personatges)
print(Artistes)
"""
# insertar los documentos en la colección
collection = db['Editorial']
collection.insert_many(Editorial)

collection = db['Publicacio']
collection.insert_many(Publicacio)

collection = db['Personatge']
collection.insert_many(Personatges)

collection = db['Colleccio']
collection.insert_many(Colleccio)

collection = db['Artista']
collection.insert_many(Artistes)