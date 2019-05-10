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

    def test_is_branch(self):
        # Create node with no children
        price = 0.04
        node = TrieNode(price)
        assert node.is_branch() is False
        # Attach 2 with price
        node.children[2] = TrieNode(0.5)
        assert node.is_branch() is True

    def test_height(self):
        # Create node with no children
        price = 0.04
        node = TrieNode(price)
        assert node.height() == 0
        # Attach child node
        node.children[2] = TrieNode(0.5)
        assert node.height() == 1
        node.children[2].children[4] = TrieNode(0.6)
        assert node.height() == 2
        node.children[2].children[3] = TrieNode(0.6)
        assert node.height() == 2

class TrieTest(unittest.TestCase):

    def test_init(self):
        tree = Trie()
        assert tree.size == 0
        assert tree.is_empty() is True

    def test_init_with_list(self):
        tree = Trie([('123', 0.5), ('456', 1.2), ('78911', 0.9)])
        assert tree.height() == 5
        assert tree.size == 11
        assert tree.root.children[1].price == 0
        assert tree.root.children[1].children[2].children[3].price == 0.5
        assert tree.is_empty() is False

    def test_size(self):
        tree = Trie([('123', 0.5), ('456', 1.2), ('78911', 0.9)])
        assert tree.height() == 5
        assert tree.size == 11
        tree.insert('1234', 0.8)
        assert tree.height() == 5
        assert tree.size == 12
        tree.insert('1234', 0.9)
        assert tree.height() == 5
        assert tree.size == 12
        tree.insert('78922222', 0.8)
        assert tree.height() == 8
        assert tree.size == 17
