import requests
import time
from threading import Timer

def peticionhttp():
    response = requests.get('https://unigrasasapirest.azurewebsites.net/UNIGRASAS/api/nicknames')
    # return response.json()
    return response.status_code

def executeTimer1(peticiones):
    # print(f"-> executeTimer1 started at {time.strftime('%b %d %Y %H:%M:%S')}")
    print('--------')
    print('-> Peticiones hechas al servidor AZURE: ', peticiones)
    print('--------')
    response = peticionhttp()
    if response:
        print('Response: ', response)
        print('--------')
        executeTimer2(peticiones)

def executeTimer2(peticiones):
    print(f"-> executeTimer started at {time.strftime('%b %d %Y %H:%M:%S')}")
    timer1 = Timer(239, executeTimer1, [peticiones + 1])
    timer1.start()
    for segundo in reversed(range(0, 240)):
        print('La petición http se hara en: ', segundo, ' segundos')
        time.sleep(1)

def timer():
    executeTimer1(1)

timer()