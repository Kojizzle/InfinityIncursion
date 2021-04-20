from adventurelib import Item

class Character(Item):
  def __init__(self, name):
    super().__init__(name)
    self.nightmare = False