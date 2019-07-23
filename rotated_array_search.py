# WIP
class Solution(object):
  def search_data(self, nums, begin, end, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    pivot = (begin + end) / 2
    while begin <= end:
      if nums[pivot] == target:
        return pivot
      if nums[pivot] > target:
        if nums[begin] <= nums[pivot] and nums[begin] > target:
          return self.search_data(nums, pivot + 1, end, target)
        else:
          return self.search_data(nums, begin, pivot - 1, target)
      else:
        if nums[end] >= nums[pivot] and nums[end] < target:
          return self.search_data(nums, begin, pivot - 1, target)
        else:
          return self.search_data(nums, begin, end, target)

    return -1

  def search(self, nums, target):
    total_nums = len(nums)
    begin = 0
    end = total_nums - 1
    return self.search_data(nums, begin, end, target)
