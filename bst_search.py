# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
  def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root.val == val:
      return root

    if val < root.val:
      if root.left:
        return self.searchBST(root.left, val)
      else:
        return None

    if val > root.val:
      if root.right:
        return self.searchBST(root.right, val)
      else:
        return None

    return None
