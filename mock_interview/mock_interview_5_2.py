class Solution(object):
  def should_count_submat(self, mat):
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
      for j in range(n):
        if mat[i][j] == 0:
          return 0

    return 1

  def count_submat(self, mat, i, j, m, n):
    i_reduced_count = 0
    j_reduced_count = 0
    if m == 1 and n == 1:
      return mat[i][j]

    for x in range(i, m):
      for y in range(j, n):
        if mat[x][y] == 1:


    if i > 0:
      i_reduced_count = self.count_submat(mat, i - 1, j, m, n)

    if j > 0:
      j_reduced_count = self.count_submat(mat, i, j - 1, m, n)

    return count + i_reduced_count + j_reduced_count




  def numSubmat(self, mat):
    """
    :type mat: List[List[int]]
    :rtype: int
    """
    m = len(mat)
    if m == 0:
      return 0

    n = len(mat)
    if n == 0:
      return 0

    return self.count_submat(mat, m - 1, n - 1, m, n)


matr = [[1,0,1],
       [1,1,0],
       [1,1,0]]
s = Solution()
print s.numSubmat(matr)