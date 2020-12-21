# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if t1 is None and t2 is None:
      return None

    if t1 and t2:
      t1.val = t1.val + t2.val
      t1.left = self.mergeTrees(t1.left, t2.left)
      t1.right = self.mergeTrees(t1.right, t2.right)
      return t1
    elif t2 and not t1:
      t1 = t2
      return t1
    else:
      return t1
