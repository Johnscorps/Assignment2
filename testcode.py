import requests
import json
def test1():
	response = requests.get("http://35.195.89.128:8080/containers").json()
	print('Test GET /containers')
	print(response)
def test2():
	response = requests.get("http://35.195.89.128:8080/containers?state=running").json()
        print('Test GET /containers?state=running')
        print(response)
def test3():
	response = requests.get("http://35.195.89.128:8080/images").json()
        print('Test GET /images')
        print(response)

test1()
test2()
test3()
