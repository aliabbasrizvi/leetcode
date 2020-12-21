class ProductOfNumbers(object):

  def __init__(self):
    self.nums = []
    self.cached_prod = 0
    self.cached_k = -1

  def add(self, num):
    """
    :type num: int
    :rtype: None
    """
    self.nums.append(num)
    self.cached_prod = 0
    self.cached_k = -1

  def getProduct(self, k):
    """
    :type k: int
    :rtype: int
    """
    if k == 0:
      return 0
    prod = 1
    start = self.cached_k

    if self.cached_k == -1:
      for idx in range(len(self.nums) - 1, len(self.nums) - 1 - k, -1):
        prod *= self.nums[idx]
        if prod == 0:
          return 0
    else:
      if k == self.cached_k:
        return self.cached_prod
      if k > self.cached_k:
        prod = self.cached_prod
      else:
        prod = 1
        start = 0
      for idx in range(len(self.nums) - start - 1, len(self.nums) - start - 1 - (k - start), -1):
        prod *= self.nums[idx]
        if prod == 0:
          return 0

    self.cached_prod = prod
    self.cached_k = k
    return prod
