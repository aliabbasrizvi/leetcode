# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def get_inorder_traversal(self, root, L, R):
    if root == None:
      return []

    if root.left and root.left.val >= L:
      left_tree = self.get_inorder_traversal(root.left, L, R)
    else:
      left_tree = []

    if root.right and root.right.val <= R:
      right_tree = self.get_inorder_traversal(root.right, L, R)
    else:
      right_tree = []
    tree = left_tree + [root.val] + right_tree
    return tree

  def rangeSumBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """
    bin_tree_array = self.get_inorder_traversal(root, L, R)
    return sum(bin_tree_array)
