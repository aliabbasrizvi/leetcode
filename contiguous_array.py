# WIP
class Solution(object):
  def findMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counts = []
    count_0 = 0
    count_1 = 0
    counts.append((0, 0))
    for num in nums:
      if num == 0:
        count_0 += 1
      if num == 1:
        count_1 += 1
      counts.append((count_0, count_1))

    max_length = 0
    for i in xrange(len(counts)):
      for j in xrange(i, len(counts)):
        diff_0 = counts[j][0] - counts[i][0]
        diff_1 = counts[j][1] - counts[i][1]
        if diff_0 == diff_1:
          if j - i > max_length:
            max_length = j - i

    return max_length
