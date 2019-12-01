import math

class Solution(object):

  def convert_array_to_number(self, arr):
    num = 0
    for idx, val in enumerate(arr):
      num += math.pow(2, idx) * val

    return num


  def readBinaryWatch(self, num):
    """
    :type num: int
    :rtype: List[str]
    """
    if num >= 9:
      return []

    digits_to_num = {}
    for idx in xrange(7):
      digits_to_num[idx] = []

    minutes_array = [0] * 6
    hours_array = [0] * 4

    all_minutes = []
    all_hours = []

    min_min = 0
    min_hr = 0


# s = Solution()
# s.readBinaryWatch(1)

