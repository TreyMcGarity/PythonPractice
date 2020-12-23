from bst import BST

"""
Given a binary search tree, print out the elements of the tree in order without using recursion.
"""

bst = BST(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(2)
bst.insert(6)
bst.insert(8)

bst.in_order_print()