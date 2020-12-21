class Solution(object):
  def __init__(self):
    self.results = []

  def add_to_results(self, new_interval):
    added = False
    for res in self.results:
      # Check new is larger
      if new_interval[0] <= res[0] and new_interval[1] >= res[1]:
        res[0] = new_interval[0]
        res[1] = new_interval[1]
        added = True
        break

      # Check res is larger
      if new_interval[0] > res[0] and new_interval[1] < res[1]:
        added = True
        break

      if ((new_interval[0] >= res[0] and new_interval[0] <= res[1]) or
          (new_interval[1] >= res[0] and new_interval[1] <= res[1])):
        res[0] = min(new_interval[0], res[0])
        res[1] = max(new_interval[1], res[1])
        added = True
        break

    if added is False:
      self.results.append(new_interval)


  def merge(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    self.results = []
    intervals = sorted(intervals, key=lambda x: x[0])
    for interval in intervals:
      self.add_to_results(interval)

    return self.results
