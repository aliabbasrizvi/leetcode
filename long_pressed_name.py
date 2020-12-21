class Solution(object):
  def isLongPressedName(self, name, typed):
    """
    :type name: str
    :type typed: str
    :rtype: bool
    """

    name_idx = 0
    typed_idx = 0

    name_len = len(name)
    typed_len = len(typed)

    while name_idx < name_len and typed_idx < typed_len:
      count_char_name = 0
      count_char_typed = 0

      current_char = name[name_idx]
      if current_char != typed[typed_idx]:
        return False

      while name_idx < name_len and current_char == name[name_idx]:
        name_idx += 1
        count_char_name += 1

      while typed_idx < typed_len and current_char == typed[typed_idx]:
        typed_idx += 1
        count_char_typed += 1

      if count_char_typed < count_char_name:
        return False

    if name_idx != name_len or typed_idx != typed_len:
      return False
    return True
