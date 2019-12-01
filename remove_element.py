class Solution(object):
  def swap_number(self, nums, current, swap_contender):
    temp = nums[swap_contender]
    nums[swap_contender] = nums[current]
    nums[current] = temp

  def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if len(nums) == 0:
      return 0
    swap_contender = len(nums) - 1
    while swap_contender >= 0 and nums[swap_contender] == val:
      swap_contender -= 1
    idx = 0
    while idx < swap_contender:
      if nums[idx] == val:
        self.swap_number(nums, idx, swap_contender)
        swap_contender -= 1
        while nums[swap_contender] == val:
          swap_contender -= 1
      idx += 1

    return swap_contender + 1
