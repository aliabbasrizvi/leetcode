class Solution(object):
  # WIP
  def intToRoman(self, num):
    roman_number = ""
    while num != 0:
      m_count = int(num / 1000)
      num = num / 1000


  def update_number(self, existing_roman_number, count, literal):
    updated_roman_number = existing_roman_number