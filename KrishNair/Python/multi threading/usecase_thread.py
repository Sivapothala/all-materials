'''
Real-World example - Multithreading for I/O-bound Tasks
Scenario : Web Scraping
Web Scraping often involves making numerous network requests to 
fetch the web pages. these tasks are I/O-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly 
improve the performance by allowing multiple web pages to be fetched concurrently.     

'''

'''
https://python.langchain.com/v0.1/docs/get_started/introduction/
https://python.langchain.com/v0.1/docs/get_started/installation/
https://python.langchain.com/v0.1/docs/use_cases/tool_use/

'''

import requests
import threading
from bs4 import BeautifulSoup

urls =[
    "https://python.langchain.com/v0.1/docs/get_started/introduction/",
    "https://python.langchain.com/v0.1/docs/get_started/installation/",
    "https://python.langchain.com/v0.1/docs/use_cases/tool_use/"
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'Fetched length : {len(soup.text)} characters from {url}')

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All the Web pages Fetched.")