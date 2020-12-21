class Solution(object):
  def __init__(self):
    self.subs = set()

  def process_subsets(self, nums):
    if len(nums) == 0:
      self.subs.add(str(nums))
      return

    self.subs.add(str(nums))
    for idx in range(len(nums)):
      self.process_subsets(list(set(nums) - set([nums[idx]])))

  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    self.process_subsets(nums)
    self.subs = list(self.subs)
    solution = []
    for sub in self.subs:
      solution.append(eval(sub))
    return solution
