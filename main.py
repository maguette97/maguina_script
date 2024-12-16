from PIL import Image
import os

OG_PATH = os.path.join('.', 'original_images')
EDITED_PATH = os.path.join('.', 'edited_images')

size_600 = (600, 600)

for f in os.listdir(OG_PATH):
    i = Image.open(f"{OG_PATH}/{f}")
    f_name, f_extension = os.path.splitext(f)

    i.thumbnail(size_600, Image.ANTIALIAS)
    i.save(f"{EDITED_PATH}/{f_name}{f_extension}")


