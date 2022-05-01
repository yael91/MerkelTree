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

def build_merkle_tree(leaves):
    depth = math.log(len(leaves), 2)
    return build_tree(leaves, depth, 0)


# recursive function to build the tree
def build_tree(leaves, depth, current_depth):
    # we reached to leaf
    if current_depth == depth:
        return Tree(leaves[0])

    leaves_number = len(leaves)
    half = int(leaves_number/2)
    sub_leaves_left = leaves[0:half]
    sub_leaves_right = leaves[half:]
    # recursive call to left subTree & right subTree
    left = build_tree(sub_leaves_left, depth, current_depth + 1)
    right = build_tree(sub_leaves_right, depth, current_depth + 1)
    # the concatenating of both sides
    concatenating = left.root + right.root
    # sha256 HASH
    hash_result = hashlib.sha256(concatenating.encode())
    return Tree(str(hash_result.hexdigest()), left, righ






def main():


main()