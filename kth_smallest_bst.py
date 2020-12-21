# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def get_node_count(self, root):
    if root is None:
      return 0

    if root.left is None and root.right is None:
      return 1

    return self.get_node_count(root.left) + self.get_node_count(root.right) + 1


  def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """

    total_left_nodes = self.get_node_count(root.left)
    total_right_nodes = self.get_node_count(root.right)

    if k - 1 < total_left_nodes:
      return self.kthSmallest(root.left, k)
    elif k - 1 > total_left_nodes:
      return self.kthSmallest(root.right, k - total_left_nodes - 1)
    else:
      return root.val
