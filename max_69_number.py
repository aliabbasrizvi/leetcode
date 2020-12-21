class Solution(object):
  def maximum69Number(self, num):
    """
    :type num: int
    :rtype: int
    """
    str_num = str(num)
    digits = [char for char in str_num]
    max_num = []
    flipped = False

    for digit in digits:
      if not flipped and digit == '6':
        max_num.append('9')
        flipped = True
      else:
        max_num.append(digit)

    max_num = ''.join(max_num)
    return int(max_num)
