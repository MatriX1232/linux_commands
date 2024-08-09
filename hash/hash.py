import sys
import hashlib


FLAG = ""
ALGORITHM = ""


def hash_file(filename, ALGORITHM):
    """This function returns the SHA-1 hash
    f the file passed into it"""

    h = None
    match ALGORITHM:
        case "-SHA1":    h = hashlib.sha1()
        case "-SHA224":  h = hashlib.sha224()
        case "-SHA256":  h = hashlib.sha256()
        case "-SHA384":  h = hashlib.sha384()
        case "-SHA512":  h = hashlib.sha512()
        case "-MD5":     h = hashlib.md5()
        case _:          print("Algorithm not recognized!")

    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex representation of digest
    return h.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Bad usage: hash -PATH/STR <path/str> -SHA1/SHA224/SHA256/SHA384/SHA512/MD5 -LOWER/UPPER")
        exit(-1)
    FLAG = sys.argv[1]
    ALGORITHM = sys.argv[3]

    try:    CASE = sys.argv[4]
    except: CASE = "-UPPER"

    RET = ""

    if FLAG == "-STR":
        match ALGORITHM:
            case "-SHA1":     RET = (hashlib.sha1(sys.argv[2].encode()).hexdigest())
            case "-SHA224":   RET = (hashlib.sha224(sys.argv[2].encode()).hexdigest())
            case "-SHA256":   RET = (hashlib.sha256(sys.argv[2].encode()).hexdigest())
            case "-SHA384":   RET = (hashlib.sha384(sys.argv[2].encode()).hexdigest())
            case "-SHA512":   RET = (hashlib.sha512(sys.argv[2].encode()).hexdigest())
            case "-MD5":      RET = (hashlib.md5(sys.argv[2].encode()).hexdigest())
            case _:           print("Algorithm not recognized!")

    elif FLAG == "-PATH":
        RET = (hash_file(sys.argv[2], ALGORITHM))

    if CASE == "-LOWER":
        print(RET.lower())
    elif CASE == "-UPPER":
        print(RET.upper())