class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """

    total_digits = len(digits)
    if len(digits) == 0:
      return digits

    digits[-1] += 1
    carry_over = digits[-1] / 10
    digits[-1] %= 10
    for i in range(total_digits - 2, -1, -1):
      if carry_over == 0:
        break

      digits[i] += carry_over
      carry_over = digits[i] /10
      digits[i] %= 10

    if carry_over == 1:
      digits.insert(0, 1)

    return digits
