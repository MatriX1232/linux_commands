import argparse
import os
from Colors import Color


def get_char_diff(line1: str, line2: str) -> int:
    diff_count = 0
    length = len(line1)
    delta = len(line1) - len(line2)

    if delta > 0: length = len(line2)

    for i in range(0, length):
        if line1[i] != line2[i]:    diff_count += 1
    if len(line1) != len(line2):
        diff_count += abs(delta)
    return diff_count, delta


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file1", type=str, help="Name of the first file")
    parser.add_argument("file2", type=str, help="Name of the second file")

    args = parser.parse_args()

    path = os.getcwd()
    file1 = open(os.path.join(path, args.file1), 'r')
    file2 = open(os.path.join(path, args.file2), 'r')
    while True:
        line1 = file1.readline()
        line2 = file2.readline()
        if line1 != line2:
            diff_count, delta = get_char_diff(line1, line2)
            print(Color.red(f'< {line1}'))
            if delta < 0:  print(Color.red("< 0"))
            else:          print(Color.red(f'< {delta}'))
            print(Color.green(f'> {line2}'))
            if delta >= 0:   print(Color.green(f'> {delta}'))
            else:            print(Color.green(f'> 0'))
        if not line1 or not line2:  break
    file1.close()
    file2.close()