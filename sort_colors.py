class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    counts = [0, 0, 0]
    for num in nums:
      counts[num] += 1

    val = 0
    upd_idx = 0
    while val < 3:
      for idx in range(counts[val]):
        nums[upd_idx] = val
        upd_idx += 1
      val += 1

    return nums
