# WIP
class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 0:
      return s
    longest_palindrome = s[0]
    for i in xrange(2, len(s) + 1):
      for j in xrange(len(s) - i + 1):
        current_str = s[j:j + i]
        if current_str == current_str[::-1]:
          longest_palindrome = current_str

    return longest_palindrome
