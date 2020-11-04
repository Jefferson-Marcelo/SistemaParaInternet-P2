class Node:
  def __init__(self, date):
    self.__date = date
    self.__next = None
  
  # get
  @property
  def date(self):
    return self.__date
  
  # set
  @date.setter
  def date(self, newDate):
    self.__date = newDate

  # get
  @property
  def next(self):
    return self.__next
  
  # set
  @next.setter
  def next(self, newDate):
    self.__next = newDate
