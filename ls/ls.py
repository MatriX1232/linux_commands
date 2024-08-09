import sys
import os
import argparse
from Colors import Color

import os
import argparse
import time


def get_longest_name(entries: list) -> int:
    max_len = 0
    for entry in entries:
        if len(entry) > max_len:    max_len = len(entry)
    return max_len


def colors_of_ext(fileName: str, add_spaces: str) -> None:
    # print(fileName.split('.')[-1])
    match fileName.split('.')[-1]:
        case "bat" | "exe" | "msi" | "ini":     print(Color.magenta(fileName), end=add_spaces)
        case "png" | "jpg" | "jpeg":            print(Color.yellow(fileName), end=add_spaces)
        case "mp4" | "mkv":                     print(Color.green(fileName), end=add_spaces)
        case _:                                 print(Color.white(fileName), end=add_spaces)

# Function to list directory contents
def list_directory_contents(path, all_files=False, long_format=False):
    try:
        entries = os.listdir(path)

        # If not showing hidden files, filter them out
        if not all_files:
            entries = [entry for entry in entries if not entry.startswith('.')]

        max_len = get_longest_name(entries)
        print(Color.red(f'Total: {len(entries)}'))
        for entry in entries:
            if long_format:
                entry_path = os.path.join(path, entry)
                size = os.path.getsize(entry_path)
                m_time = os.path.getmtime(entry_path)
                f_stat = str(oct(os.stat(entry_path).st_mode)[-3:])

                add_spaces = (max_len - len(entry) + 1) * ' '
                add_spaces = add_spaces + '\t'

                if os.path.isdir(entry_path):
                    f_stat = 'd-' + f_stat
                    print(Color.blue(f_stat), end="\t")
                    print(Color.cyan(entry), end=add_spaces)
                    print(Color.blue("0"), end="\t")
                else:
                    f_stat = '--' + f_stat
                    print(Color.blue(f_stat), end="\t")
                    colors_of_ext(entry, add_spaces)
                    # print(Color.white(entry), end=add_spaces)
                    print(Color.blue(str(size)), end='\t')
                print(Color.green(time.ctime(m_time)))
                # print(f"{size:>10} {entry}")
            else:
                print(entry)

    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
    except NotADirectoryError:
        print(f"ls: '{path}' is not a directory")
    except PermissionError:
        print(f"ls: cannot open directory '{path}': Permission denied")


# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="List directory contents (like 'ls').")
parser.add_argument("path", nargs="?", default=".", help="Directory to list (default is current directory).")
parser.add_argument("-a", "--all", action="store_true", help="Include hidden files (starting with '.').")
parser.add_argument("-l", "--long", action="store_true", help="Use a long listing format.")

# Parse arguments
args = parser.parse_args()

# List directory contents
list_directory_contents(args.path, all_files=args.all, long_format=args.long)

# if __name__ == "__main__":
    # path = sys.argv[0].split('\\')[:-1]
    # path = '\\'.join(path)
    # print(os.getenv())
    # for dirpath, dirnames, filenames in os.walk(path):
    #     for dirName in dirnames:    print(Color.blue(dirName))
    #     for fileName in filenames:  print(Color.white(fileName))
    