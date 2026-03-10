import requests
from datetime import datetime

print(datetime.now())

print("hello world")
# response = requests.get("https://api.github.com")
# print(response.status_code)

name = "deepak"

print(f"hello {len(name)}")


age = 20

if age > 40:
    print("you are older then me")
else:
    print("execute anyway")

    def getName(name):
        print(f"name - {name}")
        return name


getN = getName("neharika")
print(getN)


for i in range(10,13):
    print(i)
