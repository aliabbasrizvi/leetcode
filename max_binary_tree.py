# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
  def constructMaximumBinaryTree(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
      return None

    max_val = nums[0]
    max_val_idx = 0

    for idx in range(1, len(nums)):
      if nums[idx] > max_val:
        max_val = nums[idx]
        max_val_idx = idx

    node = TreeNode(max_val)
    node.left = self.constructMaximumBinaryTree(nums[:max_val_idx])
    node.right = self.constructMaximumBinaryTree(nums[max_val_idx + 1:])

    return node
