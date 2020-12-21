class Solution(object):
  def reconstructQueue(self, people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    people = sorted(people, key=lambda x: x[0])
    people = sorted(people, key=lambda x: x[1])

    i = 0
    j = 0




s = Solution()
print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])