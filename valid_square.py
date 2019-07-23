class Solution(object):
  def get_square_dist(self, p1, p2):
    return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])

  def validSquare(self, p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    d12 = self.get_square_dist(p1, p2)
    d13 = self.get_square_dist(p1, p3)
    d14 = self.get_square_dist(p1, p4)
    d23 = self.get_square_dist(p2, p3)
    d24 = self.get_square_dist(p2, p4)
    d34 = self.get_square_dist(p3, p4)

    val_to_count = {}
    val_to_count[d12] = val_to_count.get(d12, 0) + 1
    val_to_count[d13] = val_to_count.get(d13, 0) + 1
    val_to_count[d14] = val_to_count.get(d14, 0) + 1
    val_to_count[d23] = val_to_count.get(d23, 0) + 1
    val_to_count[d24] = val_to_count.get(d24, 0) + 1
    val_to_count[d34] = val_to_count.get(d34, 0) + 1

    if len(val_to_count) != 2:
      return False

    all_keys = sorted(val_to_count.keys())
    all_values = sorted(val_to_count.values())
    if all_values[0] == 2 and all_values[1] == 4 and all_keys[1] == all_keys[0] * 2:
      return True

    return False
