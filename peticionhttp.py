import requests
import time
from threading import Timer

def peticionhttp():
    response = requests.get('https://unigrasasapirest.azurewebsites.net')
    # return response.json()
    return response.status_code

def executeTimer(peticiones):
    response = peticionhttp()
    if response:
        print('--------\n', 'Response: ', response)
        print('--------\n', '-> Peticiones realizadas al servidor AZURE: ', peticiones, '\n--------')
        time.sleep(1)
        print(f"-> executeTimer started at {time.strftime('%b %d %Y %H:%M:%S')}")
        timer1 = Timer(5, executeTimer, [peticiones + 1])
        timer1.start()
        for segundo in reversed(range(0, 4)):
            time.sleep(1)
            print('La petición http se hara en: ', segundo, ' segundos')

executeTimer(1)