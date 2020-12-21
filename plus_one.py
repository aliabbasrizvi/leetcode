class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    carry_over = False
    for idx in range(len(digits) - 1, -1, -1):
      if idx == len(digits) - 1 or carry_over:
        digits[idx] += 1
        if digits[idx] > 9:
          carry_over = True
        else:
          carry_over = False
        digits[idx] %= 10
      else:
        break

    if carry_over:
      digits.insert(0, 1)
    return digits
