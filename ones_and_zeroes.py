# WIP
class Solution(object):
  def findMaxForm(self, strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    strs.sort(key=len)
    count = 0
    for s in strs:
      count_0 = s.count('0')
      count_1 = s.count('1')
      if m - count_0 >= 0 and n - count_1 >= 0:
        m -= count_0
        n -= count_1
        count += 1

    return count

s = Solution()
print s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3)
print s.findMaxForm(["10", "0", "1"], 1, 1)
