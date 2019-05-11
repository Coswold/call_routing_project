#!python

from trie import Trie
from logger import Logger
import sys
import re

def read (txt):
    f= open(txt, "r")
    contents = f.read()
    f.close()
    contents = contents.replace('+', '')
    contents = re.split(',|\n', contents)

    return contents

def main(paths, phone_numbers):
    logger = Logger("route-costs-3.txt")
    router = Trie()
    i = 0

    while i < len(paths) - 1:
        route = paths[i]
        price = float(paths[i + 1])
        router.insert(route, price)
        i += 2

    for number in phone_numbers:
        cost = router.search(number)
        logger.log(number, cost)

if __name__ == '__main__':
    paths = read(sys.argv[1])
    phone_numbers = read(sys.argv[2])
    main(paths, phone_numbers)
