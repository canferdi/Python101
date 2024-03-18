import requests

def makeRequest(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

targetInput = input("Enter your target website: ")
if (targetInput == "0"):
    targetInput = "google.com"

with open("subdomainlist.txt", "r") as subdomainList:
    for word in subdomainList:
        word = word.strip()
        url = "http://" + word + "." + targetInput
        response = makeRequest(url)
        if response:
            print("Found subdomain ---> " + url)

