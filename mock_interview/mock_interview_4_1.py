# FAILED.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def prepare_arr(self, arr, vals):
    if len(arr) == 0:
      return

    node = arr[0]
    if node is not None:
      vals.append(arr[0].val)
      arr.append(arr[0].left)
      arr.append(arr[0].right)
    else:
      vals.append(None)

    arr = arr[1:]
    self.prepare_arr(arr, vals)


  def trimBST(self, root, low, high):
    """
    :type root: TreeNode
    :type low: int
    :type high: int
    :rtype: TreeNode
    """
    if root is None:
      return None

    arr = [root]
    vals = []

    self.prepare_arr(arr, vals)

    trimmed_vals = []
    idx = 0
    while idx < len(vals):
      if vals[idx] is not None:
        if low <= vals[idx] and vals[idx] <= high:
          trimmed_vals.append(vals[idx], )


