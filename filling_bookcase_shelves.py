
class Solution(object):
  def get_all_shelf_configs(self, books, current_book, shelf_width, current_level, remaining_width, book_set):
    # Add book to the side
    if remaining_width - books[current_book][0] >= 0:
      self.get_all_shelf_configs(books, current_book + 1, shelf_width, current_level, remaining_width - books[current_book][0])

    # Add book to next level
    self.get_all_shelf_configs(books, current_book + 1, shelf_width, current_level + 1, shelf_width)

  def minHeightShelves(self, books, shelf_width):
    """
    :type books: List[List[int]]
    :type shelf_width: int
    :rtype: int
    """
    all_book_configs = self.get_all_shelf_configs(books, 0, shelf_width, 0, shelf_width, [])


s = Solution()
print s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4)
