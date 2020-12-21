import copy

class Solution(object):
  def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) == 0 or len(nums) == 1:
      return [nums]

    lists = []
    for idx in range(len(nums)):
      current_list = [nums[idx]]
      remaining_list = nums[:idx] + nums[idx + 1:]
      permutations = self.permute(remaining_list)
      for permutation in permutations:
        new_list = copy.deepcopy(current_list)
        new_list += permutation
        lists.append(new_list)

    return lists
