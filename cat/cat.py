import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", action="store_true", help="Print $ character at the end of line")
    parser.add_argument("file_name", type=str, help="Provide file name")
    args = parser.parse_args()

    path = os.getcwd()
    flag = args.e
    file_name = args.file_name

    file = open(os.path.join(path, file_name), 'r')
    for line in file.readlines():
        print(line, end="")
        if flag:    print("$")
        else:       print()