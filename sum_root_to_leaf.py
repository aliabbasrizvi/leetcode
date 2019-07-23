class Solution(object):
  def get_all_rev_paths(self, root):
    if root.left is None and root.right is None:
      return [[root.val]]

    left_paths = None
    right_paths = None

    if root.left is not None:
      left_paths = self.get_all_rev_paths(root.left)

    if root.right is not None:
      right_paths = self.get_all_rev_paths(root.right)

    if left_paths:
      for path in left_paths:
        path.append(root.val)

    if right_paths:
      for path in right_paths:
        path.append(root.val)

    if left_paths is None:
      return right_paths

    if right_paths is None:
      return left_paths

    return left_paths + right_paths


  def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
      return 0

    all_paths = self.get_all_rev_paths(root)

    total_sum = 0
    for path in all_paths:
      num = 0
      for idx, val in enumerate(path):
        num += val * pow(10, idx)

      total_sum += num

    return total_sum
