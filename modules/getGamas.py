import requests
import json

def gerAllGama():
    #joson-sever storage/gama_producto.json -b  5004
    try:
        peticion =  requests.get("http://154.38.171.54:5004/gama")
        data = peticion.json()
        return data
    except requests.RequestException as e:
        print("Error en la solicitud HTTP:", e)
        return []
    except ValueError as e:
        print("Error al cargar JSON:", e)
        return []
def getAllNombre():
    gamaNombre = []
    for val in getAllNombre():
        gamaNombre.append(val.get("gama"))

