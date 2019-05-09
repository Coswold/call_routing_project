class TrieTreeNode(object):

    def __init__(self, price=0):
        """Initialize this binary tree node with the given data."""
        self.price = price
        self.children = [None] * 10

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'TrieTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (all decimals are None)."""
        for child in self.children:
            if child != None:
                return False
        return True

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.is_leaf() == False

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        left1 = 0
        right1 = 0
        # TODO: Check if left child has a value and if so calculate its height
        if self.left != None:
            left1 = 1 + self.left.height()
        # TODO: Check if right child has a value and if so calculate its height
        if self.right != None:
            right1 = 1 + self.right.height()
        # Return one more than the greater of the left height and right height
        if left1 > right1:
            return left1
        elif right1 >= left1:
            return right1
