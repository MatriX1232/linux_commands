import sys

from PIL import Image
import os
from Colors import Color

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(Color.red("BAD ARGUMENTS!"))
        print(Color.red("USAGE: ./imgQuality <file_name> <quality> [-s]"))
        exit(-1)

    path = os.getcwd()
    fileName = sys.argv[1]
    fileQuality = int(sys.argv[2])
    try:    ret_silent = sys.argv[3]
    except: ret_silent = None

    img = Image.open(os.path.join(path, fileName))
    fileName = fileName.split('.')
    new_name = ""
    for i in range(0, len(fileName) - 1):
        new_name += fileName[i]

    new_name += f'_q{fileQuality}.'
    new_name += fileName[-1]

    if ret_silent != "-s":
        print("PATH: ", path)
        print("fileName: ", fileName)
        print("imgFormat: ", fileQuality)
        print("New file_name: ", new_name)
    img.save(os.path.join(path, new_name), quality=1)
    img.close()