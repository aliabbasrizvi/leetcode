class Solution(object):
  def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 1:
      return nums[0]

    max_sum = nums[0]
    temp_sum = nums[0]

    for idx in range(1, len(nums)):
      temp = nums[idx]


      max_sum = max(max_sum, temp_sum)

    return max_sum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([0]))