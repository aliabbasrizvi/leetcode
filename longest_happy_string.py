class Solution(object):
  def __init__(self):
    self.res = ''
    self.prev_char = None

  def longestDiverseString(self, a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: str
    """
    if a == 0 and b == 0 and c == 0:
      result = self.res
      self.prev_char = None
      self.res = ''
      return result

    if self.prev_char is None:
      if a >= b and b >= c:
        chars_to_add = min(a, 2)
        self.prev_char = 'a'
        self.res += 'a' * chars_to_add
        return self.longestDiverseString(a - chars_to_add, b, c)
      if b >= a and a >= c:
        chars_to_add = min(b, 2)
        self.prev_char = 'b'
        self.res += 'b' * chars_to_add
        return self.longestDiverseString(a, b - chars_to_add, c)
      if c >= b and c >= a:
        chars_to_add = min(c, 2)
        self.prev_char = 'c'
        self.res += 'c' * chars_to_add
        return self.longestDiverseString(a, b, c - chars_to_add)
    elif self.prev_char == 'a':
      if b > c:
        chars_to_add = min(b, 2)
        if chars_to_add > 0:
          self.prev_char = 'b'
          self.res += 'b' * chars_to_add
          return self.longestDiverseString(a, b - chars_to_add, c)
      else:
        chars_to_add = min(c, 2)
        if chars_to_add > 0:
          self.prev_char = 'c'
          self.res += 'c' * chars_to_add
          return self.longestDiverseString(a, b, c - chars_to_add)
    elif self.prev_char == 'b':
      if a > c:
        chars_to_add = min(a, 2)
        if chars_to_add > 0:
          self.prev_char = 'a'
          self.res += 'a' * chars_to_add
          return self.longestDiverseString(a - chars_to_add, b, c)
      else:
        chars_to_add = min(c, 2)
        if chars_to_add > 0:
          self.prev_char = 'c'
          self.res += 'c' * chars_to_add
          return self.longestDiverseString(a, b, c - chars_to_add)
    elif self.prev_char == 'c':
      if b > a:
        chars_to_add = min(b, 2)
        if chars_to_add > 0:
          self.prev_char = 'b'
          self.res += 'b' * chars_to_add
          return self.longestDiverseString(a, b - chars_to_add, c)
      else:
        chars_to_add = min(a, 2)
        if chars_to_add > 0:
          self.prev_char = 'a'
          self.res += 'a' * chars_to_add
          return self.longestDiverseString(a - chars_to_add, b, c)

    result = self.res
    self.prev_char = None
    self.res = ''
    return result


s = Solution()
print s.longestDiverseString(0, 4, 7)
