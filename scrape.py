#!/usr/bin/env python
import requests
import random
import re
from bs4 import BeautifulSoup
"""Script searches for random Wikipedia articles starting from a base link to the set depth."""

__author__ = "SpacerZ"
__date__ = "7/23/2021"

WIKI_REGEX = re.compile(r'.*\/wiki\/[^:%]*')
# ! Config values
STARTING_POINT_URL = "https://en.wikipedia.org/wiki/Social_commerce"
DEPTH = 20

def scrape_wikipedia_webpages(url):
    webpage_data = requests.get(url)
    soup = BeautifulSoup(webpage_data.content, 'html.parser')
    webpage_a_elements = soup.find(id='bodyContent').find_all('a')
    potential_webpages = []

    for a in webpage_a_elements:
        if WIKI_REGEX.search(str(a)):
            potential_webpages += a

    # ! Throws an error if no other links were scraped.
    if len(potential_webpages) == 0:
        raise Exception('No links were scraped!')

    random.shuffle(potential_webpages)
    selected_link = str(potential_webpages[0])
    selected_link = selected_link.replace(" ", "_")

    output = "https://en.wikipedia.org/wiki/" + selected_link
    print('Output value : ' + output)
    return output

final_webpage_url = STARTING_POINT_URL
for search_depth in range(DEPTH):
    final_webpage_url = scrape_wikipedia_webpages(final_webpage_url)

print(final_webpage_url)
