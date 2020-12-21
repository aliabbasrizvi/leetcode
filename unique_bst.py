class Solution(object):
  def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 2:
      return n

    left_count = self.numTrees(n - 1)
    right_count = self.numTrees(n - 1)

    return left_count + right_count + 1


s = Solution()
