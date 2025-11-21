import sys

from PIL import Image

images = []

for arg in sys.argv:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costmes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

# This code take costume1 and costume2 to make a little annimation with the images