from DataStructure.LinkedList.Node import CNode

class CLinkedList(object):
    # This linkedlist only stores different elements
    # and does not store the None element.
    # Each element in the list is unique.

    def __init__(self, head = None):
        self.head = head
        self.count = 0

    def __str__(self):
        tmp = ""
        p = self.head
        while p != None:
            tmp += str(p.value)
            tmp += ","
            p = p.next
        if len(tmp) > 0:
            Res = tmp[:len(tmp)-1]
        return Res

    def IsFound(self, value):
        p = self.head
        while p is not None:
            if p.value is value:
                return True
            p = p.next
        return False

    def InsertFirst(self, node):
        if node == None:
            return
        if self.IsFound(node) is True:
            return
        node.SetNextNode(self.head)
        self.head = node
        self.count += 1

    def InsertLast(self, node):
        if node == None:
            return
        if self.IsFound(node) is True:
            return
        node.SetNextNode(None)
        p = self.head
        if p is None:
            self.head = node
        else:
            while p.next is not None:
                p = p.next
            p.next = node

    def Remove(self, value):
        p = self.head
        if p.value is value:
            self.head = self.head.next
            del p
            return
        q = p
        p = p.next
        while p is not None:
            if p.value is value:
                q.next = p.next
                del p
                return
            q = p
            p = p.next

    def GetSize(self):
        return self.count