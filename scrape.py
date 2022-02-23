#!/usr/bin/env python
import requests
import random
from bs4 import BeautifulSoup
"""Script searches for random Wikipedia articles starting from a base link to the set depth."""

__author__ = "SpacerZ ; Cody Boynton"
__date__ = "7/23/2021"

STARTING_POINT_URL = "https://en.wikipedia.org/wiki/United_States_Naval_Research_Laboratory"
# ! Change this to search deeper into Wikipedia from the starter URL.
DEPTH = 1

def scrape_wikipedia_webpages(url):
    webpage_data = requests.get(url)

    soup = BeautifulSoup(webpage_data.content, 'html.parser')

    title = soup.find(id='firstHeading')

    potential_webpages = soup.find(id='bodyContent').find_all('a')

    random.shuffle(potential_webpages)

    selected_webpage = 0

    for webpage in potential_webpages:
        if webpage['href'].find('/wiki/') == -1:
            continue

        selected_webpage = webpage
        break

    return "https://en.wikipedia.org" + selected_webpage['href']

final_webpage_url = STARTING_POINT_URL
for search_depth in range(DEPTH):
    final_webpage_url = scrape_wikipedia_webpages(final_webpage_url)

print(final_webpage_url)
