class Solution(object):
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    qualifying_nums = []
    required_freq = float (len(nums) / 3.0)
    num_to_count = {}
    for num in nums:
      num_to_count[num] = num_to_count.get(num, 0) + 1
      if num_to_count[num] > required_freq and num not in qualifying_nums:
        qualifying_nums.append(num)

    return qualifying_nums
