import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass


username = input("Enter your username NOW: ")
password = getpass("Input the password if you DARE!: ")

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"


payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
