class Solution(object):
  def thousandSeparator(self, n):
    """
    :type n: int
    :rtype: str
    """
    separated_string = ''
    while n >= 1000:
      part = n % 1000
      if separated_string == '':
        separated_string = str(part).zfill(3)
      else:
        separated_string = str(part).zfill(3) + '.' + separated_string
      n = n / 1000

    if separated_string != '':
      return str(n) + '.' + separated_string

    return str(n)
