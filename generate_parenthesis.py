class Solution(object):
  def get_all_combinations(self, n):
    all_combinations = []
    if n == 0:
      return all_combinations
    else:
      all_combinations = ['(', ')']
    for i in xrange(1, n * 2):
      left_addition = ['(' + combo for combo in all_combinations]
      right_addition = [')' + combo for combo in all_combinations]
      all_combinations = left_addition + right_addition
    return all_combinations

  def get_all_valid_combinations(self, n):
    all_combinations = self.get_all_combinations(n)
    all_valid_combinations = []
    for combo in all_combinations:
      left_parenthesis = combo.count('(')
      right_parenthesis = combo.count(')')
      if left_parenthesis - right_parenthesis != 0:
        continue

      parenthesis_count = 0
      for idx in xrange(len(combo)):
        if parenthesis_count < 0:
          break
        if combo[idx] == '(':
          parenthesis_count += 1
        if combo[idx] == ')':
          parenthesis_count -= 1

      if parenthesis_count == 0:
        all_valid_combinations.append(combo)

    return all_valid_combinations

  def generateParenthesis(self, n):
    return self.get_all_valid_combinations(n)
