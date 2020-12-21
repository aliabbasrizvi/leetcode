class StockSpanner(object):

  def __init__(self):
    self.stock_span = []
    self.stock_prices = []


  def next(self, price):
    """
    :type price: int
    :rtype: int
    """

    total_count = len(self.stock_prices)
    if total_count == 0:
      self.stock_span.append(1)
      self.stock_prices.append(price)
      return self.stock_span[-1]

    idx = total_count - 1
    count = 1
    while idx >= 0 and self.stock_prices[idx] <= price:
      count += self.stock_span[idx]
      idx -= self.stock_span[idx]

    self.stock_span.append(count)
    self.stock_prices.append(price)
    return count
