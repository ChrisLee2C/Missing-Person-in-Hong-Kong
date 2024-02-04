from config import *
from datetime import date,timedelta
import time
import requests
import xml.etree.ElementTree as ET

def data_request_get():
    timedif=date.today()-timedelta(days=2)
    yesterday=timedif.strftime("%Y%m%d")
    resp=requests.get(TIMESTAMP_API_HEAD+f"&start={yesterday}&end={yesterday}")
    timestamps=resp.json()["timestamps"][0]
    status_code=0
    while status_code!=200:
        print("Get data with the following api: ")
        print(DATA_API_HEAD+f"&time={timestamps}")
        resp=requests.get(DATA_API_HEAD+f"&time={timestamps}")
        if resp.status_code==200:
            xml_content=resp.content
            tree=ET.ElementTree(ET.fromstring(xml_content))
            root=tree.getroot()
            return root
        else:
            status_code=resp.status_code
            print('error with '+str(resp.status_code))
            time.sleep(3)