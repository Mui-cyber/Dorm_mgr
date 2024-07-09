import requests

def network_logout():
    requests.post("http://10.100.1.5/eportal/InterFace.do?method=logout")
