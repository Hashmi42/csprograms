class Queue (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def enqueue (self, item):
      self.items.insert(0,item)

   def dequeue (self):
      return self.items.pop ()

   def size (self):
      return len(self.items)

   def peek (self):
      return self.items [len(self.items)-1]



def palChecker(st):
    chardecque = Deque()

    for ch in st:
        chardeque.addRear(ch)

    stillEqual = True

    While chardeque.size() > 1 stillEqual:
        first = chardecque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual



