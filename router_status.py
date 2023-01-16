import requests


def get_status(ip):
    try:
        requests.get(ip)
        return True
    except:
        return False
