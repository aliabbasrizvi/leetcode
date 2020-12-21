class Solution(object):
  def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    m = len(A)
    n = len(A[0])

    for i in range(m):
      for j in range(n / 2):
        temp = A[i][j]
        A[i][j] = A[i][n - 1 - j]
        A[i][n - 1 - j] = temp

    for i in range(m):
      for j in range(n):
        if A[i][j] == 1:
          A[i][j] = 0
        else:
          A[i][j] = 1

    return A
