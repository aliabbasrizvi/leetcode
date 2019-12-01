class Solution(object):
  def largestSumAfterKNegations(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """

    if K == 0:
      return sum(A)

    sorted_nums = sorted(A)

    neg_nums = []
    pos_nums = []
    zeroes = []
    new_A = []

    for num in sorted_nums:
      if num < 0:
        neg_nums.append(num)
      elif num > 0:
        pos_nums.append(num)
      else:
        zeroes.append(num)

    for num in neg_nums:
      if K > 0:
        new_A.append(num * -1)
      else:
        new_A.append(num)
      K -= 1

    if len(zeroes) > 0:
      K = 0

    if K > 0:
      if K % 2 == 1:
        if new_A and pos_nums[0] > new_A[-1]:
          new_A[-1] *= -1
        else:
          pos_nums[0] *= -1

    return sum(new_A) + sum(pos_nums)
