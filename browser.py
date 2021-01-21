# coding: utf-8
import os
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

page_stack = deque()

while True:
    args = sys.argv
    command_arg = args[1]
    if not os.path.exists(f"/Users/christiane/PycharmProjects/Text-Based Browser/Text-Based Browser/task/{command_arg}"):
        os.mkdir(f"/Users/christiane/PycharmProjects/Text-Based Browser/Text-Based Browser/task/{command_arg}")
    url = input()
    if url.endswith(".com") or url.endswith(".org"):
        if not url.startswith("https://"):
            url = "https://" + url
            url_for_file = ''.join(c for c in url if c not in ":/.-")
        if os.path.exists(f"/Users/christiane/PycharmProjects/Text-Based Browser/Text-Based Browser/task/{command_arg}/{url_for_file}"):
            with open(f"{command_arg}/{url_for_file}", "r") as f:
                contents = f.read()
                print(contents)
                page_stack.append(contents)
        else:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            urls = soup.find_all('a')
            with open(f"{command_arg}/{url_for_file}", "w", encoding='utf-8') as f:
                for a in soup.find_all():
                    if a in urls:
                        print(Fore.BLUE + a.get_text())
                        f.write(Fore.BLUE + a.get_text())
                    else:
                        print(a.get_text())
                        f.write(a.get_text())
    elif url == "back":
        if len(page_stack) > 1:
            page_stack.pop()
            print(page_stack.pop())
        else:
            break
    elif url == "exit":
        page_stack.clear()
        break
    else:
        page_stack.clear()
        print("Error: Incorrect URL")






