class Solution(object):
  def maxIncreaseKeepingSkyline(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    total_addition = 0
    maxTB = [0] * len(grid)
    maxRL = [0] * len(grid)
    for i in xrange(len(grid)):
      for j in xrange(len(grid[0])):
        if grid[i][j] > maxRL[j]:
          maxRL[j] = grid[i][j]
        if grid[i][j] > maxTB[i]:
          maxTB[i] = grid[i][j]

    for i in xrange(len(grid)):
      for j in xrange(len(grid[0])):
        total_addition += min(maxTB[i], maxRL[j]) - grid[i][j]

    return total_addition
