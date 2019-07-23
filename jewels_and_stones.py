class Solution(object):
  def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    stone_to_count_map = {}
    total_jewel_count = 0
    for stone in S:
      stone_to_count_map[stone] = stone_to_count_map.get(stone, 0) + 1

    for jewel in J:
      total_jewel_count += stone_to_count_map.get(jewel, 0)

    return total_jewel_count
