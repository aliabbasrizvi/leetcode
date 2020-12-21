class Solution(object):
  def compare_strings(self, str_arr):
    total_strings = len(str_arr)
    for i in range(1, total_strings):
      if str_arr[i] != str_arr[i - 1]:
        return False

    return True

  def repeatedSubstringPattern(self, s):
    """
    :type s: str
    :rtype: bool
    """
    str_len = len(s)
    for i in range(1, str_len / 2 + 1):
      str_arr = []
      j = 0
      while j < str_len:
        str_arr.append(s[j:j + i])
        j += i

      if self.compare_strings(str_arr):
        return True

    return False
