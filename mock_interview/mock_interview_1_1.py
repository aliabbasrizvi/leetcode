class Solution(object):
  def rotateString(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    doubled_A = A + A
    return B in doubled_A and len(A) == len(B)
