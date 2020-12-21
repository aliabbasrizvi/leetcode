class Solution(object):
  def get_return_form(self, start, end):
    if start == end:
      return str(start)
    else:
      return '{}->{}'.format(start, end)

  def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    summary_ranges = []
    if len(nums) == 0:
      return summary_ranges

    idx = 0
    while idx < len(nums):
      start = nums[idx]
      while idx + 1 != len(nums) and nums[idx + 1] - nums[idx] == 1:
        idx += 1

      summary_ranges.append(self.get_return_form(start, nums[idx]))
      idx += 1

    return summary_ranges
