class Solution(object):
  def removeKdigits(self, num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    if num == '':
      return '0'

    if k == 0 or int(num) == 0:
      return str(int(num))

    remove_idx = 0
    for idx in xrange(1, len(num)):
      if num[idx] > num[remove_idx]:
        remove_idx = idx
      elif num[idx] == num[remove_idx]:
        remove_idx = idx
      else:
        break

    num = num[:remove_idx] + num[remove_idx + 1:]
    return self.removeKdigits(num, k - 1)
