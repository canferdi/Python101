import requests
from bs4 import BeautifulSoup

targetUrl = "https://atilsamancioglu.com"
foundLinks = []


def makeRequest(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def crawl(url):
    links = makeRequest(url)
    for link in links.find_all("a"):
        foundLink = link.get("href")
        if foundLink:
            if "#" in foundLink:
                foundLink = foundLink.split("#")[0]
            if targetUrl in foundLink and foundLink not in foundLinks:
                foundLinks.append(foundLink)
                print(foundLink)
                # recursive
                crawl(foundLink)


crawl(targetUrl)
