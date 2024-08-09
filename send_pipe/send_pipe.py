import io
import sys
from Colors import Color
import subprocess


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Color.red("BAD ARGUMENTS!"))
        print(Color.red("USAGE: ./send_pipe <string_to_send>"))
        exit(-1)

    to_send = sys.argv[1]
    process = subprocess.Popen(
        ['cmd', '/C'],  # Start cmd.exe and run an empty command
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Send data to the subprocess's stdin
    output, error = process.communicate(input=to_send)

    # ps = subprocess.Popen(['echo', 'Hello :)'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # output, error = ps.communicate(to_send)