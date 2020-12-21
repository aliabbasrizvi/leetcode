class Solution(object):
  def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = len(nums)
    if count == 1:
      return 0

    for idx, num in enumerate(nums):
      if idx == 0 and num > nums[idx + 1]:
        return idx
      elif idx == count - 1 and num > nums[idx - 1]:
        return idx
      elif 0 < idx < count and num > nums[idx - 1] and num > nums[idx + 1]:
        return idx
