"""
Задание 3. Дан ресурс в интернете, его адрес вводится с клавиатуры.
Напишите функцию, которая будет одновременно отправлять 1 000 GET-запросов к нему.
С помощью библиотеки tqdm отобразите progress-bar, отображающий количество уже отправленных запросов.

требуется установить aiohttp и tqdm
"""

import aiohttp
import asyncio
import time
from tqdm import tqdm


start_time = time.time()

url = input('Enter URL: ')

async def get(url):
    async with aiohttp.ClientSession() as session:
        for _ in tqdm(range(1000)):
            async with session.get(url) as resp:
                await resp.read()


asyncio.run(get(url))

print(f"--- {time.time() - start_time} ---")
