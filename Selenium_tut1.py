"""
First use of Selenium web driver
"""
# Firefox browsers
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
my_first_script = webdriver.Firefox()
my_first_script.get("http://www.google.com")
assert "Google" in my_first_script.title
search_bar = my_first_script.find_element_by_name('q')
search_bar.send_keys('VP Records')
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
album_home = my_first_script.find_element_by_link_text("Albums")
album_home.click()
time.sleep(3)
my_first_script.quit()