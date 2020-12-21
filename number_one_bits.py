class Solution(object):
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    str_n = str(n)
    print n
    return str_n.count('1')

s = Solution()
print s.hammingWeight(00000000000000000000000000001011)
print s.hammingWeight(00000000000000000000000010000000)
print s.hammingWeight(11111111111111111111111111111101)