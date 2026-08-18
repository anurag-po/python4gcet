class A:
  def __init__(self):
    self.val1 = 0
    self.val2 = 0

  def val1change(self, n):
    self.val1 = n
  def display(self):
    print(self.val1)


myobject = A()
myobject.val1change(3)
myobject.display()
