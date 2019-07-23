class Solution(object):
  def reverseVowels(self, s):
    vowels = 'aeiouAEIOU'
    vowels_in_string = []
    for idx in xrange(len(s)):
      if s[idx] in vowels:
        vowels_in_string.append(idx)

    total_vowels = len(vowels_in_string)
    if total_vowels == 0 or total_vowels == 1:
      return s

    string_list = list(s)
    for idx in xrange(len(vowels_in_string) / 2):
      temp_char = string_list[vowels_in_string[idx]]
      string_list[vowels_in_string[idx]] = string_list[vowels_in_string[total_vowels - idx - 1]]
      string_list[vowels_in_string[total_vowels - idx - 1]] = temp_char

    return ''.join(string_list)
