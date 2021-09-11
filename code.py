import requests

import base64

with open('code.py', 'rb') as f:
    data = f.read()

email="pentamarch2000@gmail.com"
email_bytes = email.encode("ascii")
password = base64.b64encode(email_bytes)

headers = {'Name':"Aditi Srivastava",'Email':"pentamarch2000@gmail.com",'College':'PICT','StudentId':'I2K18102518','Filename':'code.py','Password':password}
r = requests.put("https://prod-24.centralindia.logic.azure.com/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM",
headers=headers,data=data)
print(r.text)
print(r.status_code)

