import requests
import json

def gerAllGama():
    #joson-sever storage/gama_producto.json -b  5004
    peticion = requests.get("")
    data= peticion.json()
    return data
def getAllNombre():
    gamaNombre = []
    for val in getAllNombre():
        gamaNombre.append(val.get("gama"))

