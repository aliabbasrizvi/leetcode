class Solution(object):
  def findDisappearedNumbers(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    missing_nums = []
    array_len = len(nums)
    for num in nums:
      nums[(num - 1) % array_len] += array_len

    print nums
    for idx, num in enumerate(nums):
      if num <= array_len:
        missing_nums.append(idx + 1)

    return missing_nums
