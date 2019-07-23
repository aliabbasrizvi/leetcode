class Solution(object):
  def is_palindrome(self, part_str):
    if part_str == part_str[::-1]:
      return True

    return False

  def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    for idx in len(s)



s = Solution()
print s.partition('aab')
