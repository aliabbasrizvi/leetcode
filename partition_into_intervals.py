class Solution(object):
  def partitionDisjoint(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    max_num = A[0]
    max_idx = 0
    for idx, num in enumerate(A):
      if num > max_num:
        max_idx = idx
        max_num = num

    
    return max_idx


s = Solution()
print s.partitionDisjoint([5,0,3,8,6])
print s.partitionDisjoint([1,1,1,0,6,12])
