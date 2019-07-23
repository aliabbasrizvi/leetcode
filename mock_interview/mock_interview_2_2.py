class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    rev_nums = nums[::-1]

    left_prod = [1]
    right_prod = [1]
    prods = []
    for idx in xrange(len(nums) - 1):
      left_prod.append(nums[idx] * left_prod[idx])

    for idx in xrange(len(rev_nums) - 1):
      right_prod.append(rev_nums[idx] * right_prod[idx])

    right_prod = right_prod[::-1]
    for idx in xrange(len(nums)):
      prods.append(left_prod[idx] * right_prod[idx])
    return prods
