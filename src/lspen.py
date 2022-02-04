from sys import argv
import base64

name = argv[-1]

with open(f"{name}.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    with open(f"{name}.lsp", "wb") as lsp_file:
        lsp_file.write(encoded_string)