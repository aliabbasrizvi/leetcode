class Solution(object):
  NUM_TO_LETTER = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  }

  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    combos = []
    if len(digits) == 0:
      return []

    if len(digits) == 1:
      return list(self.NUM_TO_LETTER.get(digits))

    return_values = self.letterCombinations(digits[1:])
    for char in self.NUM_TO_LETTER.get(digits[0]):
      for value in return_values:
        combos.append(char + value)

    return combos
