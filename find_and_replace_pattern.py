import collections

class Solution(object):
  def build_pattern(self, word_for_pattern):
    char_to_position = collections.OrderedDict()
    for idx, char in enumerate(list(word_for_pattern)):
      if char in char_to_position:
        char_to_position[char].append(idx)
      else:
        char_to_position[char] = [idx]

    return char_to_position.values()

  def findAndReplacePattern(self, words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    pattern_to_compare = self.build_pattern(pattern)
    similar_words = []
    for word in words:
      if len(word) != len(pattern):
        continue
      pattern_for_word = self.build_pattern(word)
      if pattern_for_word == pattern_to_compare:
        similar_words.append(word)

    return similar_words
