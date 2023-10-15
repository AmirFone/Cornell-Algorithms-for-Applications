'''
Problem 3a
'''

class Node:
    def __init__(self, val:int, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, x):
        new_node = Node(x,None)
        if self.root is None:
            self.root = new_node
        elif x < self.root.val:
            new_node.next = self.root
            self.root = new_node
        else:
            temp = self.root
            while temp.next is not None and temp.next.val < x:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def search(self, x):   
        temp= self.root
        while temp:
            if temp.val==x:
                return temp
            temp=temp.next
        
    def delete(self, x):
        if self.root is None:
            return
        if self.root.val == x:
            self.root = self.root.next
        else:
            temp=self.root
            prv= None
            while temp and temp.val != x:
                prv=temp
                temp=temp.next
            if temp is not None:
                prv.next = temp.next