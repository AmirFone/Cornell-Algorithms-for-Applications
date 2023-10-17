from random import randint

class Node:
    """A node from a skip list"""    
    def __init__(self, height = 0, elem=None):
        self.val = elem
        self.next = [None]*height

class SkipList:

    def __init__(self, maxHeight, probability):
        self._root = Node(maxHeight, None)
        self.maxHeight = maxHeight
        self.p = probability
        self.first = None
        self.len = 0

    @property
    def root(self):
        # need to do this because of the way the tests are written
        return self.first or self._root

    def search(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        node = update[0].next[0] if update[0] else None
        if node != None and node.val == elem:
            return node
        return None

    def insert(self, elem):
        node = Node(self.randomHeight(), elem)

        if self.first is None:
          self.first = node

        while len(self._root.next) < len(node.next):
            self._root.next.append(None)
            
        self.maxHeight = max(self.maxHeight, len(node.next))

        update = self.updateList(elem)
        for i in range(len(node.next)):
            node.next[i] = update[i].next[i] if update[i] else None
            update[i].next[i] = node

        self.len += 1

    def delete(self, elem):

        update = self.updateList(elem)
        x = self.search(elem, update)

        if x != None:
            for idx, item in enumerate(update):
                if item and item.next[idx] == x:
                    item.next[idx] = x.next[idx]
                    if self._root.next[idx] == item:
                        self.maxHeight -= 1
            self.len -= 1

            if x == self.first:
                self.first = self.first.next[0]

    def randomHeight(self):
        height = 1
        while randint(0, self.maxHeight-1) < self.maxHeight*self.p:
            height += 1
        return height

    def updateList(self, elem):
        update = [None]*self.maxHeight
        x = self._root

        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and (x.next[i].val < elem if x.next[i] else False):
                x = x.next[i]
            update[i] = x
        return update
