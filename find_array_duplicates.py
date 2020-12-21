class Solution(object):
  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    duplicate_nums = []
    for idx, val in enumerate(nums):
      # Make number greater by at least length of array
      nums[val % len(nums) - 1] += len(nums)

    for idx, num in enumerate(nums):
      if num > 2 * (len(nums)):
        duplicate_nums.append(idx + 1)

    return duplicate_nums
