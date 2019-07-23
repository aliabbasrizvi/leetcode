class Solution(object):
  def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    if m == 0:
      return False

    n = len(matrix[0])
    if n == 0:
      return False

    if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
      return False

    x = 0
    y = n - 1
    while x >= 0 and x < m and y < n and y >= 0:
      if target == matrix[x][y]:
        return True
      if target > matrix[x][y]:
        x += 1
      else:
        y -= 1

    return False
