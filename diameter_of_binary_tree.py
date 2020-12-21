# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

  def get_height(self, root):
    left_height = 0
    right_height = 0

    if root is None:
      return 0

    if root.left is None and root.right is None:
      return 1

    if root.left:
      left_height = 1 + self.get_height(root.left)

    if root.right:
      right_height = 1 + self.get_height(root.right)

    return max(left_height, right_height)

  def diameterOfBinaryTree(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
      return 0

    current_diameter = self.get_height(root.left) + self.get_height(root.right)
    left_diameter = self.diameterOfBinaryTree(root.left)
    right_diameter = self.diameterOfBinaryTree(root.right)

    return max(current_diameter, left_diameter, right_diameter)
