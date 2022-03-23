from PIL import Image
import os

def resize(im,new_width):
    width,height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width, new_height))
    return resized_image

files = os.listdir("images")  #pasta de imagens
extensions = ['jpg','jpeg','png','gif',]
for file in files:
    ext = file.split(".")[-1]
    if ext in extensions:
        im = Image.open("images/"+file) #caminho da pasta de imagens
        im_resized = resize(im,300) #redimensionar
        filepath = f"images/{file}.png" #caminho da pasta de imagens
        im_resized.save(filepath)
