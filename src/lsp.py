import requests
import random
import base64
import os
from os.path import exists
from argparse import ArgumentParser
from PIL import Image


def choose_img():
    if exists("img-list.txt"):
        with open("img-list.txt", encoding="utf-8") as img_list:
            name = random.choice(img_list.readlines())
            url = f"https://raw.githubusercontent.com/SatinWuker/lsp/MASTER/lsp-db/{name}.lsp"

            with open(f"{name}.png", 'wb') as img_f:
                lsp_content = requests.get(url).content
                img_f.write(base64.b64decode(lsp_content))

                return f"{name}.png"

    else:
        exit("找不到文件 [img-list.txt]")


def main():
    img_name = choose_img()

    print(f"显示图片 [{img_name}]")

    image = Image.open(img_name)
    image.show()
    os.remove(img_name)



if __name__ == "__main__":
    main()