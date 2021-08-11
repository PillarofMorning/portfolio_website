import sqlite3
import datetime
import random
import PIL
from PIL import Image, ImageDraw, ImageOps, ImageFont


def get_concat_h_blank(im1, im2, color=(0, 0, 0)):
    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im

def image_correction(image, name, tense, position):
    im1 = Image.open(image)
    im1 = ImageOps.expand(im1, border=55, fill='black')
    if position == 'reversed':
        im1 = im1.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    I1 = ImageDraw.Draw(im1)
    myfont = ImageFont.truetype('CormorantInfant-Bold.ttf', 18)
    I1.text((112, 410), name, font=myfont, fill=(255, 255, 255))
    I1.text((138, 20), tense, font=myfont, fill=(255, 255, 255))
    return im1


def user_daily_read():

    conn = sqlite3.connect("tarot.db")

    c = conn.cursor()

    c.execute("SELECT Name FROM Tarot_Cards")

    card_names = c.fetchall()

    reading = {}

    co=0
    for card in sorted(card_names, key=lambda x: random.random())[0:3]:
        reading[card[0]] = {}
        reading[card[0]]['tense'] = ['past', 'present', 'future'][co]
        reading[card[0]]['position'] = random.choice(['upright', 'reversed'])
        reading[card[0]]['url'] = ''
        co+=1


    for card in reading.keys():
        c.execute('SELECT Image_Url FROM Tarot_Cards WHERE name = "' + card + '"')
        i = c.fetchone()
        reading[card]['url'] = i[0]

    img_list = []

    for tcimage in reading.keys():
        img_list.append(image_correction(reading[tcimage]['url'], tcimage,  reading[tcimage]['tense'], reading[tcimage]['position']))

    get_concat_h_multi_blank(img_list).save('D:\\antoa\\tarot_sql\\reading.jpg')








user_daily_read()