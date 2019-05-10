#!python

from trie import Trie, TrieNode
import unittest


class TrieNodeTest(unittest.TestCase):

    def test_init(self):
        price = 0.04
        node = TrieNode(price)
        assert len(node.children) == 10
        assert node.children[0] is None
        assert node.children[1] is None

    def test_is_leaf(self):
        # Create node with no children
        price = 0.04
        node = TrieNode(price)
        assert node.is_leaf() is True
        # Attach 2 with price
        node.children[2] = TrieNode(0.5)
        assert node.is_leaf() is False
