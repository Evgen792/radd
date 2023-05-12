from captcha.image import ImageCaptcha
from random import choice
pattern = 'q2we2rty3'

image_captcha = ImageCaptcha(width=300, height=200)

image_captcha.write(pattern, 'captcha.jpg')