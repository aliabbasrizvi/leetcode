class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
  def intervalIntersection(self, A, B):
    """
    :type A: List[Interval]
    :type B: List[Interval]
    :rtype: List[Interval]
    """
    a_idx = 0
    b_idx = 0

    int_list = []
    while(a_idx < len(A) or b_idx < len(B)):
      if A[a_idx].start < B[b_idx].start:



s = Solution()
print s.intervalIntersection([Interval(0,2),Interval(5,10),Interval(13,23), Interval(24,25)],
                             [Interval(1,5),Interval(8,12),Interval(15,24), Interval(25,26)])