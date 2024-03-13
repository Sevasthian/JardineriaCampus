import json



def postProducto(data):
    import requests
    #json-server storage/producto.json -b 5002
    peticion = requests.post("http://172.16.100.145:5003", data=json.dumps(data))
    res = peticion.json()
    return res