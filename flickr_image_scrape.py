from bs4 import BeautifulSoup as bs
import urllib.request
import re
import random

# smaller the faster, but with repeated images
IMAGES_TO_ITERATE_OVER = 10

'''
Searches over flickr using Beautiful Soup, parses the query to get the relevant picture.
input
tag: image you are looking for
return
url of the image
'''
def get_image_url_from_flickr(tag):
    # search flickr to get the relevant image
    base_url =  "https://www.flickr.com/search/?text="
    get_url = "https://www.flickr.com/search/?text="+tag

    # bs4 magic
    html = urllib.request.urlopen(get_url).read()
    soup = bs(html,'html.parser')
    div_tags = soup('div')

    # randomizing the image
    count = random.randint(1,IMAGES_TO_ITERATE_OVER)
    for item in div_tags:
        class_attribute = item.get('class')  
        if class_attribute and 'photo-list-photo-view' in class_attribute:
            style_attrs = item.attrs['style']
            if style_attrs:
                photo_url = style_attrs.split("//")[1]
                photo_url = photo_url[:-1]
                if count == 0:
                    return photo_url
                count = count - 1
    
    # Control should never reach here ideally
    # throw a print error along with returning a None, which is handled by the caller
    return None



if __name__=="__main__":
    print(get_image_url_from_flickr("CLEAR"))
