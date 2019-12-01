class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    sorted_nums = sorted(nums)
    i = 0
    j = len(nums) - 1
    found = False
    while i < j:
      sum = sorted_nums[i] + sorted_nums[j]
      if sum == target:
        found = True
        break
      if sum < target:
        i += 1
      else:
        j -= 1

    solution = [-1, -1]
    if found:
      for idx in xrange(len(nums)):
        if nums[idx] == sorted_nums[i] and solution[0] == -1:
          solution[0] = idx
        elif nums[idx] == sorted_nums[j] and solution[1] == -1:
          solution[1] = idx

    return sorted(solution)
