import random

class Solution(object):

  def __init__(self, nums):
    """
    :type nums: List[int]
    """
    self.nums = []
    self.original_nums = []
    for num in nums:
      self.nums.append(num)
      self.original_nums.append(num)

  def reset(self):
    """
    Resets the array to its original configuration and return it.
    :rtype: List[int]
    """
    self.nums = []
    for num in self.original_nums:
      self.nums.append(num)

    return self.nums

  def shuffle(self):
    """
    Returns a random shuffling of the array.
    :rtype: List[int]
    """
    for idx in range(len(self.nums)):
      random_idx = random.randint(0, len(self.nums) - 1)
      temp = self.nums[idx]
      self.nums[idx] = self.nums[random_idx]
      self.nums[random_idx] = temp

    return self.nums
