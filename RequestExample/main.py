import requests
import json

# GET veri alırken
userInput = input("Enter ID: ")
getUrl = f"https://jsonplaceholder.typicode.com/todos/{userInput}"

getResponse = requests.get(getUrl)
print(getResponse.json())

# POST veri yollarken
toDoItem = {"userId": 2, "title": "my to do", "completed": False}
postUrl = "https://jsonplaceholder.typicode.com/todos"
# optional header
headers = {"Content-Type": "application/json"}
postResponse = requests.post(postUrl, data=json.dumps(toDoItem), headers=headers)
print(postResponse.json())

