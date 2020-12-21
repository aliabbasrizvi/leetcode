class Solution(object):
  def find(self, nums, target, start, end):
    if start == end:
      if start >= 0 and nums[start] == target:
        return start
      else:
        return -1

    if target > nums[end] or target < nums[start]:
      return -1

    mid = (start + end) / 2
    if target < nums[mid]:
      return self.find(nums, target, start, mid - 1)
    elif target > nums[mid]:
      return self.find(nums, target, mid + 1, end)
    else:
      return mid


  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    return self.find(nums, target, 0, len(nums) - 1)
