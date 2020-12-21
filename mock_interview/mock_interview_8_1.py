# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def get_sum(self, root, is_left):
    if root is None:
      return 0

    if root.right is None and root.left is None:
      if is_left:
        return root.val
      else:
        return 0

    sum_left = self.get_sum(root.left, True) + self.get_sum(root.right, False)
    return sum_left

  def sumOfLeftLeaves(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return self.get_sum(root, False)
