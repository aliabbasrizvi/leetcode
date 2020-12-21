# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def get_leaf_order(self, root):
    left = []
    right = []
    if root is None:
      return []

    if root.left is None and root.right is None:
      return [root.val]

    if root.left:
      left = self.get_leaf_order(root.left)

    if root.right:
      right = self.get_leaf_order(root.right)

    return left + right


  def leafSimilar(self, root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool
    """

    root1_leaf_order = self.get_leaf_order(root1)
    root2_leaf_order = self.get_leaf_order(root2)

    if len(root1_leaf_order) != len(root2_leaf_order):
      return False

    for idx, val in enumerate(root1_leaf_order):
      if root2_leaf_order[idx] != val:
        return False

    return True
