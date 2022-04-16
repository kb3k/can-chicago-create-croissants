#!/usr/bin/python3

from PIL import Image

image = Image.open('croissant_toolarge.jpeg')
new_image = image.resize((400, 400))
new_image.save('croissant.jpeg')

print('image resized successfully;', image.size)

