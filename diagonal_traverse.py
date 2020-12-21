class Solution(object):
  def findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    m = len(matrix)
    if m == 0 or m == 1:
      return [] if m == 0 else matrix[0]
    n = len(matrix[0])
    diagonal_order = []
    i = 0
    j = 0
    going_up = True
    while i < m or j < n:
      diagonal_order.append(matrix[i][j])
      if i == m - 1 and j == n - 1:
        break
      if going_up:
        if i - 1 >= 0 and j + 1 < n:
          i -= 1
          j += 1
        else:
          going_up = False
          if j + 1 == n and i < m:
            i += 1
          if i == 0 and j + 1 < n:
            j += 1
      else:
        if i + 1 < m and j - 1 >= 0:
          i += 1
          j -= 1
        else:
          going_up = True
          if i + 1 == m and j < m:
            j += 1
          if j == 0 and i + 1 < m:
            i += 1

    return diagonal_order
