class Solution(object):
  def get_all_rev_paths(self, root):
    if root.left is None and root.right is None:
      return [[str(root.val)]]

    left_paths = None
    right_paths = None

    if root.left is not None:
      left_paths = self.get_all_rev_paths(root.left)

    if root.right is not None:
      right_paths = self.get_all_rev_paths(root.right)

    if left_paths:
      for path in left_paths:
        path.append(str(root.val))

    if right_paths:
      for path in right_paths:
        path.append(str(root.val))

    if left_paths is None:
      return right_paths

    if right_paths is None:
      return left_paths

    return left_paths + right_paths


  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root is None:
      return []

    all_paths = self.get_all_rev_paths(root)

    str_paths = []
    for path in all_paths:
      str_paths.append('->'.join(path[::-1]))

    return str_paths
