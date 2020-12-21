class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    has_ones = False
    m = len(matrix)
    if m > 0:
      n = len(matrix[0])
    else:
      return 0
    max_area = 0

    for i in range(m):
      for j in range(n):
        matrix[i][j] = int(matrix[i][j])
        if matrix[i][j] == 1:
          has_ones = True

    if has_ones:
      max_area = 1
    else:
      return 0

    if m == 1 or n == 1:
      return 1

    for i in range(1, m):
      for j in range(1, n):
        if matrix[i][j] == 1:
          matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
          if matrix[i][j] > max_area:
            max_area = matrix[i][j]

    return max_area * max_area
