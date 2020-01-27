import json
import requests
import os
AUTH_ENDPOINT="http://127.0.0.1:8000/api/auth/jwt/"
ENDPOINT="http://127.0.0.1:8000/api/status/"
data={
    'username':'saiaditya',
    'password':'vanevane'
}
r=requests.post(AUTH_ENDPOINT,data=data)
print(r.json())