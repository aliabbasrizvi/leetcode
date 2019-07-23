class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    sorted_string_to_strings_map = {}

    for word in strs:
      map_key = ''.join(sorted(word))
      if map_key in sorted_string_to_strings_map:
        sorted_string_to_strings_map[map_key].append(word)
      else:
        sorted_string_to_strings_map[map_key] = [word]

    list_of_words = []
    for anagram_list in sorted_string_to_strings_map.values():
      list_of_words.append(anagram_list)

    return list_of_words
