class Solution(object):
  def __init__(self):
    self.known_solutions = {}

  def get_key(self, m, n):
    return '{},{}'.format(m, n)

  def lookup_solution(self, m, n):
    return self.known_solutions.get(self.get_key(m, n))

  def store_solution(self, m, n, value):
    self.known_solutions[self.get_key(m, n)] = value

  def uniquePaths(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    value = self.lookup_solution(m, n)
    if value:
      return value

    if m == 1 and n == 1:
      return 1

    if m == 0 or n == 0:
      return 0

    total_paths = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    self.store_solution(m, n, total_paths)
    return total_paths

