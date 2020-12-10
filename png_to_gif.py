from PIL import Image
from os import listdir as dir


for folder in dir("src/img"):
    if len(contents := dir("src/img/" + folder)) == 0:
        continue
    for file in contents:
        if file.endswith(".png"):
            im = Image.open(f"src/img/{folder}/{file}").save(f"src/img/{folder}/{file.split('.')[0] + '.gif'}")
