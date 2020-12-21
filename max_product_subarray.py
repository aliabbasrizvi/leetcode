class Solution(object):
  def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_prod = nums[0]
    local_max = nums[0]
    local_min = nums[0]
    for num in nums[1:]:
      temp = local_max
      local_max = max(num, num * local_max, num * local_min)
      local_min = min(num, num * temp, num * local_min)

      max_prod = max(max_prod, local_max)

    return max_prod
