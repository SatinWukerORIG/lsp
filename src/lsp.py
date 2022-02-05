import requests
import random
import base64
import os
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from PIL import Image
from termcolor import colored

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}


def choose_img():

    # Read directories under lsp-db
    re = requests.get("https://github.com/SatinWuker/lsp/tree/MASTER/lsp-db", headers=headers)
    soup = BeautifulSoup(re.text, 'html.parser')

    img_list = []      # all of the images names in the LSP database

    for link in soup.find_all("a", class_="js-navigation-open Link--primary"):
        img_list.append(link.get_text())

    # Randomly choose one image in the img_list
    name = random.choice(img_list)
    # Get the url of the chosen image
    url = f"https://raw.githubusercontent.com/SatinWuker/lsp/MASTER/lsp-db/{name}"
    print("访问 " + colored(url, 'green'))

    # Download the image
    with open(f"TempLSPimg.png", 'wb') as img_f:
        lsp_content = requests.get(url).content
        img_f.write(base64.b64decode(lsp_content))

        return "TempLSPimg.png"


def main():
    img_name = choose_img()

    print(f"显示图片 [{colored(img_name, 'red')}]")

    # Show image
    image = Image.open(img_name)
    image.show()
    os.remove(img_name)


if __name__ == "__main__":
    main()
