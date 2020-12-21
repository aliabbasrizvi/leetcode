class Solution(object):
  def transpose(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    t_A = [[]] * len(A[0])
    for i in range(len(A[0])):
      t_A[i] = [0] * len(A)

    for i in range(len(A)):
      for j in range(len(A[0])):
        t_A[j][i] = A[i][j]

    return t_A
