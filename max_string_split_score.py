class Solution(object):
  def maxScore(self, s):
    """
    :type s: str
    :rtype: int
    """
    max_score = 0
    for idx in range(1, len(s)):
      left_s = s[:idx]
      right_s = s[idx:]
      score = left_s.count('0') + right_s.count('1')
      if score > max_score:
        max_score = score

    return max_score
