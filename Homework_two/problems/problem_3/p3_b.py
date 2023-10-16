import random

class Node:
  def __init__(self, val, level): 
    self.val = val
    self.next = [None] * level

class SkipList:
  def __init__(self, max_level, p):
    self.max_level = max_level
    self.p = p 
    self.root = Node(None, max_level)  # renamed from self.root to self.root

  def random_level(self):
    level = 0
    while random.random() < self.p  and level < self.max_level - 1:  
      level += 1
    return min(level, self.max_level-1)

  def insert(self, x):
    new_level = self.random_level()
    new_node = Node(x, new_level)
    update = [self.root] * self.max_level

    current = self.root
    
    for i in reversed(range(new_level + 1)):
        while i < len(current.next) and current.next[i] and current.next[i].val < x: 
            current = current.next[i]  
        update[i] = current

    # If root's value is None (which means this is 
    # the first element being inserted)
    if self.root.val is None:
        self.root = new_node
        # Assign the next pointers of the root node
        self.root.next = new_node.next
    else:
        for i in range(new_level+1):
            if i >= len(new_node.next):
                new_node.next.append(None)
            
            # Make this assignment only if `i` is within the range of `update[i].next`
            if i < len(update[i].next):
                new_node.next[i] = update[i].next[i]

            # Here also check if `i` is within the range of `update[i].next`
            if i < len(update[i].next):
                update[i].next[i] = new_node

  def search(self, x):
    current = self.root
    for i in reversed(range(self.max_level)):
      while current.next[i] and current.next[i].val < x:
        current = current.next[i]
    current = current.next[0]
    if current and current.val == x:
      return current
    else:
      return None