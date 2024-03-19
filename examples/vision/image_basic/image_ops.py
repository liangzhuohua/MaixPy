'''
    API see https://wiki.sipeed.com/maixpy/api/maix/image.html#Image
'''

from maix import image

img = image.Image(640, 480)
img = img.resize(320, 240)
img.save("test.jpg")

