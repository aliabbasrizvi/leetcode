# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
  def __init__(self):
    self.max_height = -1
    self.left_most_value = None

  def find_left_most(self, root, height):
    if root is None:
      return

    if root.left is None and root.right is None:
      if height > self.max_height:
        self.max_height = height
        self.left_most_value = root.val
      return

    self.find_left_most(root.left, height + 1)
    self.find_left_most(root.right, height + 1)

  def findBottomLeftValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.find_left_most(root, 0)
    return self.left_most_value
