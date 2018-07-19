import requests
import json
import time
def get_zip(ip, key='934aebc9a7bfa3b727bce4cccc13ce67'):
    response = requests.get('http://api.ipstack.com/%s?access_key=%s' % (ip, key))
    return response.json()

def main():
    with open('resources/characteristic.csv') as FileObj:
        arr = FileObj.readlines()
    for val in arr:
        res = get_zip(val.split(';')[2])['zip']
        if res != None:
            print(res)
#        time.sleep(1)
main()
