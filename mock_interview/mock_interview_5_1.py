class Solution(object):
  def reverseString(self, s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    start = 0
    end = len(s) - 1

    if len(s) == 0 or len(s) == 1:
      return s

    while start < end:
      temp = s[start]
      s[start] = s[end]
      s[end] = temp
      start += 1
      end -= 1

    return s
