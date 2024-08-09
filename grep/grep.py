import sys
import subprocess
from Colors import Color


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Color.red("BAD ARGUMENTS!"))
        print(Color.red("USAGE: ./grep <to_find>"))
        exit(-1)

    to_find = sys.argv[1]

    process = subprocess.Popen(
        ['cmd', '/C'],  # Echo the data back
        stdout=subprocess.PIPE,  # Capture the stdout of the subprocess
        stderr=subprocess.PIPE,
        text=True
    )

    # Read the output from the pipe (which is the echoed data)
    output, error = process.communicate()

    # input_data =
    # for line in sys.stdin:
    #     print(line)
    print(output)
    # print(sys.stdin.read())
    # print(sys.stdin.read())