class Solution(object):
  def restoreString(self, s, indices):
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    idx_to_char_map = {}
    for idx, char in enumerate(s):
      idx_to_char_map[indices[idx]] = char

    shuffled_str = ''
    for idx in range(len(s)):
      shuffled_str += idx_to_char_map[idx]

    return shuffled_str
