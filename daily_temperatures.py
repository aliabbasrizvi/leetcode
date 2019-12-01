class Solution(object):
  def dailyTemperatures(self, T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    days_left = [0] * len(T)

    if len(T) <= 1:
      return days_left

    for idx in xrange(len(T) - 2, -1, -1):
      candidate_day = idx + 1
      while T[idx] >= T[candidate_day]:
        if days_left[candidate_day] == 0:
          candidate_day = idx
          break
        candidate_day = candidate_day + days_left[candidate_day]
      days_left[idx] = candidate_day - idx
    return days_left
