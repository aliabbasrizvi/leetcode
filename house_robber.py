class Solution(object):
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
      return 0

    stolen_amount = []
    for idx, amount in enumerate(nums):
      if idx == 0:
        stolen_amount.append(nums[0])
      elif idx == 1:
        stolen_amount.append(max(nums[0], nums[1]))
      else:
        stolen_amount.append(max([stolen_amount[idx - 2] + amount, stolen_amount[idx - 1]]))

    return stolen_amount[-1]
