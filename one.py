import requests
import time
now = time.time()
for i in range(0, 100):
    r = requests.get("http://localhost")
    print(r.text)
then = time.time()
print(9.48)