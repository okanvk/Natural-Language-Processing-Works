import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import schedule
import time


def find_menu():
    response = requests.get("https://www.adu.edu.tr/tr/yemek-listesi")
    scraper = BeautifulSoup(response.text, "html.parser")
    menu = ''
    el = scraper.findAll(class_="col-lg-4")[36]
    main_div = el.findAll("div")[2]
    i = 1
    food_elements = main_div.findAll("h4")[:4]
    for food_el in food_elements:
        menu += food_el.get_text() + "\n"
    return menu


def bring_member_ids():
    member_ids = []
    with urllib.request.urlopen(
            "https://api.telegram.org/bot910851985:AAFvUErR6FpWdVDgT_V1rAvO5RQlrVKmDCs/getUpdates") as url:
        data = json.loads(url.read().decode())
        members = data['result']
        for member in members:
            member_ids.append(member['message']['chat']['id'])
    return member_ids


def job():
    members_set = set(bring_member_ids())
    menu = find_menu()

    for id in members_set:
        response = requests.get(
            f"https://api.telegram.org/bot910851985:AAFvUErR6FpWdVDgT_V1rAvO5RQlrVKmDCs/sendMessage?chat_id={id}&text={menu}")
        print(response)


schedule.every().monday.at("21:59").do(job)
schedule.every().tuesday.at("21:59").do(job)
schedule.every().wednesday.at("21:59").do(job)
schedule.every().thursday.at("21:59").do(job)
schedule.every().friday.at("21:59").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
