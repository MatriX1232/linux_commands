import random
import sys


RANGE = None
MIN = None
MAX = None
SEP = None
NO_REPEAT = None

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("BAD ARGUMENTS!")
        print(f'./random <RANGE> <MIN> <MAX> <SEP> --no-repeat', "\n<SEP> and --no-repeat not mandatory...")
        # exit(-1)

    RANGE = int(sys.argv[1])
    MIN = int(sys.argv[2])
    MAX = int(sys.argv[3])
    try:    SEP = sys.argv[4]
    except: SEP = ' '
    try:    NO_REPEAT = sys.argv[5]
    except: NO_REPEAT = None

    if NO_REPEAT is not None and (MAX - MIN < RANGE - 1):
        print("ERROR: not enough numbers to fill within range!")
        exit(-1)

    if NO_REPEAT == "--no-repeat":
        avaiable = []
        for _ in range(MIN, MAX + 1):
            avaiable.append(_)
        for _ in range(0, RANGE):
            index = random.randrange(0, len(avaiable))
            print(avaiable[index], end="")
            avaiable.pop(index)
            if _ != RANGE - 1:  print(SEP, end="")

    else:
        for _ in range(0, RANGE):
            print(random.randrange(MIN, MAX), end="")
            if _ != RANGE - 1:  print(SEP, end="")
