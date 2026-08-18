class Stack:
  def __init__(self):
    self.items = []
  def push(self, val):
    items.append(val)
  def pop(self):
    if not self.items:
      print("Stack empty")
      return
    return items.pop(-1)
  def peek(self):
    return items[-1]

  def display(self):
    for i in self.items:
      print(i)


newstack = Stack()
newstack.push(1)
newstack.push(2)
newstack.push(3)

print(newstack.peek())
print(newstack.pop())
newstack.display()

    
