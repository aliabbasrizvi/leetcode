class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
  def __init__(self):
    self.smallest_values = {}
    self.largest_values = {}

  def populate_smallest_and_largest_values(self, root):
    if root.left is None and root.right is None:
      return root.val, root.val

    if root.left is None:
      right_small, right_large = self.populate_smallest_and_largest_values(root.right)

    if root.right is None:
      left_small, left_large = self.populate_smallest_and_largest_values(root.left)

    left_small, left_large = self.populate_smallest_and_largest_values(root.left)
    right_small, right_large = self.populate_smallest_and_largest_values(root.right)





  def maxAncestorDiff(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.populate_smallest_and_largest_values(root)
