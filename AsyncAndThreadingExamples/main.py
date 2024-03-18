import threading
import requests
import time
import asyncio
import aiohttp


def getDataSync(urls):
    st = time.time()  # Start time (çalışan bilgisayarın zamanını alır)
    jsonArray = []
    for url in urls:
        jsonArray.append(requests.get(url).json())
    et = time.time()  # End time
    print(f"Execution time : {et} second")
    return jsonArray


class ThreadingDownloader(threading.Thread):
    jsonArray = []

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.jsonArray.append(response.json())
        return self.jsonArray


def getDataThreading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    et = time.time()
    elapsedTime = et - st
    print("Execution time: ", elapsedTime, "second")


async def getDataAsyncButAsWrapper(urls):
    st = time.time()
    jsonArray = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                jsonArray.append(await resp.json())

    et = time.time()
    elapsedTime = et - st
    print("Execution time: ", elapsedTime, "second")
    return jsonArray


async def getData(session, url, jsonArray):
    async with session.get(url) as resp:
        jsonArray.append(await resp.json())


async def getDataAsyncWithConcurently(urls):
    st = time.time()
    jsonArray = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(getData(session, url, jsonArray)))
        await asyncio.gather(*tasks)  #taskleri tek tek vermeye yarar *tasks

    et = time.time()
    elapsedTime = et - st
    print("Execution time: ", elapsedTime, "seconds")
    return jsonArray

urls = ["https://postman-echo.com/delay/3"] * 10
#getDataSync(urls)  # 41sn
#getDataThreading(urls)  # 5sn
#asyncio.run(getDataAsyncButAsWrapper(urls))  # 33sn
asyncio.run(getDataAsyncWithConcurently(urls)) # 5snd