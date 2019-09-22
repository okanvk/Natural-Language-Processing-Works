import requests
from bs4 import BeautifulSoup
import random

# This is a quote game.
# In this game you have to find quote's author
# Look source code and help me to add new features
# Requirements BeautifulSoup - Request

def prepareQuotes():

    page_number = 10
    tuple_of_quotes = []
    while True:
        response = requests.get("http://quotes.toscrape.com/page/{}/".format(page_number))
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.findAll(class_="quote")

        tuple_of_quotes = add_page_quotes(quotes,tuple_of_quotes)
        page_number += 1
        if page_number == 11:
            break

    return tuple_of_quotes

def select_random_quote(quotes):
    return random.choice(quotes)

def add_page_quotes(quotes,whole_quotes):
    for quote in quotes:
        text = quote.find(class_="text").get_text()
        href = quote.find("a")["href"]
        author = quote.find("small").get_text()
        whole_quotes.append((text, href, author))
    return whole_quotes

def print_quote(text):
    print("Here's a quote:\n")
    print(text)

def take_answer(guusses):
    answer = input("Who said this? Guesses Remaining: {}. ".format(guusses))
    return answer

def prepareHints(author,href):
    response = requests.get("http://quotes.toscrape.com{}".format(href))
    soup = BeautifulSoup(response.text, "html.parser")

    first_born_info = soup.find(class_ = "author-born-date").get_text()
    second_born_info = soup.find(class_ = "author-born-location").get_text()

    first_hint = "Here's a hint: The Author was born in " + first_born_info + " " + second_born_info
    second_hint = "Here's a hint: The Author's first name starts with " + author[0]
    third_hint = "Here's a hint: The Author's last name starts with " + author.split(" ")[-1][0]

    return  {"1_hint" : first_hint,"2_hint" : second_hint,"3_hint" : third_hint}

def start_game():
    game_state = "y"

    all_quotes = prepareQuotes()

    while game_state == "y":

        hint_number = 1
        guesses = 4
        selected_quote = select_random_quote(all_quotes)

        text = selected_quote[0]
        href = selected_quote[1]
        author = selected_quote[2]
        hints = prepareHints(author, href)

        while guesses != 0:

            if guesses == 4:
                print_quote(text)
            answer = take_answer(guesses)

            if answer == author:
                print("You guessed correctly! Congratulations")
                break
            else:
                guesses -= 1
                if hint_number != 4:
                    print(hints["{}_hint".format(hint_number)])
                    hint_number += 1
        game_state = input("Would you like to play again(y/n)")

if __name__ == "__main__":
    start_game()

