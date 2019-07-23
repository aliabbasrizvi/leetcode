# WIP
class Solution(object):
  def dailyTemperatures(self, T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    maximas = []
    max_location = [0] * len(T)
    for idx, val in enumerate(T):
      maximas.append((idx, val))
    maximas = sorted(maximas, key=lambda x: x[1])

    return maximas


if __name__ == '__main__':
  s = Solution()
  print s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])