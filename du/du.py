import os
import argparse


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to the folder of which you want to get sizeof")
    parser.add_argument("-units", default=False, action="store_true", help="Display units (default Bytes)")
    args = parser.parse_args()

    path = args.path
    flag = args.units
    if flag:
        print(f'{get_dir_size(path)}B')
    else:
        print(get_dir_size(path))