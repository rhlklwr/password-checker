import requests
import hashlib
import sys

url = 'https://api.pwnedpasswords.com/range/' + '0018A'
res = requests.get(url)
print(res)