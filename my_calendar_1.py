class MyCalendar(object):

  def __init__(self):
    self.meetings = []

  def book(self, start, end):
    """
    :type start: int
    :type end: int
    :rtype: bool
    """
    for meeting in self.meetings:
      if ((start > meeting[0] and start < meeting[1]) or
          (end > meeting[0] and end < meeting[1]) or
          (start <= meeting[0] and end >= meeting[1])):
        return False

    self.meetings.append((start, end))
    return True
