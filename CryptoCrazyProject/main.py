import requests

response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
# print(response)

def getCryptoData():
    if response.status_code == 200:   # Başarılıysa 200 kodu verir
        return response.json()        # Json dosyasını döndürür

cryptoData = getCryptoData()
userInput = input("Enter your cryptocurrency symbol: ")
for crypto in cryptoData:
    if userInput == crypto["currency"]:
        print(f"{userInput} price is : {crypto['price']}")
        break