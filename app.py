from PIL import Image
import os

OG_PATH = os.path.join('.', 'original_images')
EDITED_PATH = os.path.join('.', 'edited_images')

size_600 = (280, 150)

for f in os.listdir(OG_PATH):
    i = Image.open(f"{OG_PATH}/{f}")
    i = i.resize(size_600, Image.LANCZOS)
    
    f_name, f_extension = os.path.splitext(f)
    i.save(f"{EDITED_PATH}/{f_name}{f_extension}")


