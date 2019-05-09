import random
import urllib.request
def download_web_image(url):
    name = random.randrange(1,100)
    full_name = str(name) + ".jpg" #Takes name and coverts into a string
    urllib.request.urlretrieve(url,full_name)#Takes in the url then what you would name the image.
download_web_image("https://s-media-cache-ak0.pinimg.com/736x/9d/fd/28/9dfd28c977342d4f9094c10304d89f23.jpg")