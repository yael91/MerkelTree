# Shany Yael Dagan

import hashlib, math

# Binary Tree
# root is a string, left & right are Trees ('sub tree')
# when left & right are None root is a leaf
class Tree:
    def __init__ (self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

