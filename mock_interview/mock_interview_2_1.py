class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0 or len(prices) == 1:
      return 0

    lowest_price = prices[0]
    profits = [0]
    for idx in xrange(1, len(prices)):
      if prices[idx] < lowest_price:
        lowest_price = prices[idx]

      profits.append(max(profits[idx - 1], prices[idx] - lowest_price))

    return profits[-1]
