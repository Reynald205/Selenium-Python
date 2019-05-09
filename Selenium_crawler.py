"""
Selenium_crawler -- Program that runs thru album pages and identifies media I created by Reynald Walme
"""
# For Firefox
# div id="jquery_jplayer",class="jp-jplayer" needed to find media players I worked on and which albums needed one.
# id="media-player-0"> new media player
# <a class="entry-link" entry link to album
# <h1 class="artist"> ,<h1 class="page-title"> gets the album name and artist

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def vpmedia(max_pages):
    page = 1
    links = []
    crawler = webdriver.Firefox()
    while page <= max_pages:
        crawler.get('https://www.vprecords.com/albums/page/' + str(page))
        album = crawler.find_elements_by_class_name("entry-link")  # Returns list of posts on page
        for link in album:  # Takes href's from entry-link and adds them to list
            links.append(link.get_attribute("href"))

        for link in links:  # Goes through page collected url's
            href = link
            crawler.get(href)
            try:
                crawler.find_element_by_id("media-player-0")
                artist = crawler.find_element_by_class_name("artist").text
                print(href + str(" Artist: ") + artist + str(" New media player"))
            except NoSuchElementException:
                try:
                    crawler.find_element_by_id("jquery_jplayer")
                    artist = crawler.find_element_by_class_name("page-title").text
                    print(href + str(" Artist: ") + artist + str(" Old media player"))
                except NoSuchElementException:
                    try:
                        crawler.find_element_by_class_name("jp-jplayer")
                        artist = crawler.find_element_by_class_name("page-title").text
                        print(href + str(" Artist: ") + artist + str(" Older media player"))
                    except NoSuchElementException:
                        continue
        page = page + 1
        links.clear()
    crawler.close()

vpmedia(2)