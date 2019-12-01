class Solution(object):
  def heightChecker(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    if len(heights) <= 1:
      return 0
    init_height = heights[0]




s = Solution()
print s.heightChecker([1,1,4,2,1,3])
print s.heightChecker([1,1,4,7])