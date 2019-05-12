#!python

import sys
import re

def read (txt):
    f= open(txt, "r")
    contents = f.read()
    f.close()
    contents = contents.replace('+', '')
    contents = re.split(',|\n', contents)

    return contents

def main(paths, phone_number):
    i = 0
    answer = 0

    while i < len(paths) - 1:
        route = paths[i]
        price = float(paths[i + 1])
        if phone_number[0] == route[0]:
            j = 0
            while j < len(route) and j < len(phone_number):
                if phone_number[j] != route[j]:
                    break
                j += 1
            if j == len(route):
                answer = price
        i += 2

    return answer

if __name__ == '__main__':
    paths = read(sys.argv[1])
    phone_number = sys.argv[2]
    print(main(paths, phone_number))
