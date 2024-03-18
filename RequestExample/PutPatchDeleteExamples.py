import requests

getUrl = "https://jsonplaceholder.typicode.com/todos/15"

getResponse = requests.get(getUrl)
print(getResponse.json())

# PUT komple değiştirme
toDoItem15 = {"userId": 2, "title": "put title", "completed": False}
putResponse = requests.put(getUrl, json=toDoItem15)
print(putResponse.json())

# PATCH sadece 1 parametre değiştirme
toDoItemPatch15 = {"title": "Patch test"}
patchResponse = requests.patch(getUrl, json=toDoItemPatch15)
print(patchResponse.json())

#DELETE
deleteResponse = requests.delete(getUrl)
print(deleteResponse.status_code)