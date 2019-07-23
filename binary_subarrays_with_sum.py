# WIP
class Solution(object):
  def numSubarraysWithSum(self, A, S):
    """
    :type A: List[int]
    :type S: int
    :rtype: int
    """
    total_sum = sum(A)
    if S > total_sum or total_sum == 0:
      return 0

    location_1 = []
    for idx, num in enumerate(A):
      if num == 1:
        location_1.append(idx)

    num_subarrays = location_1[0] - 0 + len(A) - location_1[-1] - 1

    for idx in xrange(1, len(location_1)):
      num_subarrays += location_1[idx] - location_1[idx - 1]

    return num_subarrays





s = Solution()
print s.numSubarraysWithSum([1,0,1,0,1], 2)
location_1 = [0, 2, 4]
