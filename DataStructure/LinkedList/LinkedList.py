from DataStructure.LinkedList.Node import CNode

class CLinkedList(object):
    # This linkedlist only stores different elements
    # and does not store the None element.
    # Each element in the list is unique.

    def __init__(self, head = None):
        self.__head = head
        self.__count = 0

    def __str__(self):
        tmp = ""
        p = self.__head
        while p != None:
            tmp += str(p.GetValue())
            tmp += ","
            p = p.GetNextNode()
        if len(tmp) > 0:
            Res = tmp[:len(tmp)-1]
        return Res

    def IsFound(self, value):
        p = self.__head
        while p is not None:
            if p.GetValue() is value:
                return True
            p = p.GetNextNode()
        return False

    def InsertFirst(self, node):
        if node == None:
            return
        if self.IsFound(node) is True:
            return
        node.SetNextNode(self.__head)
        self.__head = node
        self.__count += 1

    def InsertLast(self, node):
        if node == None:
            return
        if self.IsFound(node) is True:
            return
        node.SetNextNode(None)
        p = self.__head
        if p is None:
            self.__head = node
        else:
            while p.GetNextNode() is not None:
                p = p.GetNextNode()
            p.SetNextNode(node)

    def Remove(self, value):
        p = self.__head
        if p.GetValue() is value:
            self.__head = self.__head.GetNextNode()
            del p
            return
        q = p
        p = p.GetNextNode()
        while p is not None:
            if p.GetValue() is value:
                q.SetNextNode(p.GetNextNode())
                del p
                return
            q = p
            p = p.GetNextNode()

    def GetSize(self):
        return self.__count