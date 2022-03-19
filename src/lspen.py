from sys import argv
from requests import get
import base64
import random
from string import ascii_lowercase


name = str(argv[-1])

def download(content):
    encoded_string = base64.b64encode(content)
    f_name = ''
    if 'http' in name:
        f_name = ''.join(random.choice(ascii_lowercase) for i in range(12))
    else:
        f_name = name
    with open(f"lsp{f_name}.lsplol", "wb") as lsp_file:
        lsp_file.write(bytearray(encoded_string))

if "http" in name:
    download(get(name).content)
else:
    with open(f"{name}.png", "rb") as image_file:
        download(image_file.read())
