def firstNotRepeatingCharacter(s):
  char_count = [0] * 26
  first_occurrence = [-1] * 26
  for idx, char in enumerate(s):
    char_count[ord(char) - ord('a')] += 1
    if first_occurrence[ord(char) - ord('a')] == -1:
      first_occurrence[ord(char) - ord('a')] = idx

  least_idx = len(s) + 1
  print char_count
  print first_occurrence
  for idx, count in enumerate(char_count):
    if count == 1:
      if first_occurrence[idx] < least_idx:
        least_idx = first_occurrence[idx]

  if least_idx == len(s) + 1:
    return '_'
  return s[least_idx]


print firstNotRepeatingCharacter("xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc")