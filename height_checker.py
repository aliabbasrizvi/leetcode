class Solution(object):
  def heightChecker(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    sorted_heights = sorted(heights)
    count = 0
    for idx, height in enumerate(heights):
      if height != sorted_heights[idx]:
        count += 1

    return count
