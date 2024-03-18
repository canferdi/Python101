import threading
import requests
import time


def getDataSync(urls):
    st = time.time()  # Start time (çalışan bilgisayarın zamanını alır)
    jsonArray = []
    for url in urls:
        jsonArray.append(requests.get(url).json())
    et = time.time()  # End time
    elapsedTime = et - st   # Geçen süre
    print(f"Execution time : {elapsedTime} second")

    return jsonArray


urls = ["https://postman-echo.com/delay/3"] * 10
getDataSync(urls)  # 41