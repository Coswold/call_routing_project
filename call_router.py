#!python

from trie import Trie
from logger import Logger

def main(paths, phone_numbers):
    logger = Logger()
    router = Trie(paths)
    for number in phone_numbers:
        cost = router.search(number)
        logger.log(cost)

if __name__ == '__main__':
    main()
