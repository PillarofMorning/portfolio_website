import urllib.request

for number in range(0, 78):
    urllib.request.urlretrieve("https://gfx.tarot.com/images/site/decks/crows-magick/full_size/" + str(number) + ".jpg", str(number)+".jpg"  )