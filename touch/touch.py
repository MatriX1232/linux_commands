import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="Name of created file")
    args = parser.parse_args()

    file = open(os.path.join(os.getcwd(), args.file_name), 'wb')
    file.close()