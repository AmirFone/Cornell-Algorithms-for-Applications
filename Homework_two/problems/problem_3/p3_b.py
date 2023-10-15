'''
Problem 3b
'''

import random

class Node: 
    def __init__(self, val, level):
        self.val = val
        self.next = [None] * level
        self.level = level

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.sentinel = Node(None, self.max_level)
        self.root = None

    def random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, x: int) -> None:
        new_level = self.random_level()
        new_node = Node(x, new_level)
        update = [None] * (self.max_level+1)
        current = self.root

        for i in range(self.max_level, -1, -1):
            while current and current.next[i] and current.next[i].val < x:
                current = current.next[i]
            update[i] = current

        if self.root is None or x < self.root.val:
            for i in range(new_level+1):
                new_node.next[i] = self.root
            self.root = new_node
        else:
            for i in range(new_level+1):
                if update[i] is not None:
                    new_node.next[i] = update[i].next[i]
                    update[i].next[i] = new_node


    def delete(self, x: int) -> None:
        update = [None] * (self.max_level + 1)
        current = self.root

        for i in range(self.max_level, -1, -1):
            while current.next[i] and current.next[i].val < x:
                current = current.next[i]
            update[i] = current

        current = current.next[0]

        if current and current.val == x:
            # if the node to be deleted is the root
            if x == self.root.val:
                # find the next node and make it the new root
                temp = [node for node in self.root.next if node is not None]
                self.root = min(temp, key=lambda x: x.val, default=None) if temp else None 
                
            for i in range(len(current.next)):
                if update[i].next[i] != current:
                    break
                update[i].next[i] = current.next[i]

    def search(self, x: int) -> Node:
        current = self.sentinel

        for i in range(self.max_level, -1, -1):
            while i < len(current.next) and current.next[i] and current.next[i].val < x:
                current = current.next[i]

        current = current.next[0]

        if current and current.val == x:
            return current