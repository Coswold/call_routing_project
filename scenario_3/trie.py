class TrieNode(object):

    def __init__(self, price=0):
        """Initialize this trie node."""
        self.price = price
        self.children = [None] * 10

    def __repr__(self):
        """Return a string representation of this trie node."""
        return 'TrieNode({!r})'.format(self.children)

    def is_leaf(self):
        """Return True if this node is a leaf (all children are None)."""
        for child in self.children:
            if child != None:
                return False
        return True

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.is_leaf() == False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node)."""
        height = 0
        heights = [height]
        for child in self.children:
            if child != None:
                heights.append(child.height() + 1)
        return max(heights)


class Trie(object):

    def __init__(self, number_paths=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = TrieNode()
        self.size = 0
        if number_paths != None:
            for path in number_paths:
                self.insert(path[0], path[1])

    def __repr__(self):
        """Return a string representation of this trie."""
        return 'Trie({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this trie is empty (has no nodes)."""
        return self.root.is_leaf()

    def height(self):
        """Return the height of this trie (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node)."""
        if self.is_empty() == False:
            return self.root.height()

    def search(self, number):
        """Return the price of the call for the number input."""
        current = self.root
        for num in number:
            if current.children[int(num)] is not None:
                current = current.children[int(num)]
            else:
                break

        return current.price

    def insert(self, call_path, price):
        """Insert the path of the call codes into this trie."""
        current = self.root
        for num in call_path:
            if current.children[int(num)] == None:
                current.children[int(num)] = TrieNode()
                self.size += 1
            current = current.children[int(num)]
        if current.price == 0 or current.price > price:
            current.price = price
