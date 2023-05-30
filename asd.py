import requests
import time
from stem import Signal
from stem.control import Controller


def get_current_ip():
    session = requests.session()


    try:
        r = session.get('https://spys.one/en/https-ssl-proxy/')
    except Exception as e:
        print (str(e))
    else:
        return r.text



if __name__ == "__main__":
    for i in range(1):
        print (get_current_ip())
        