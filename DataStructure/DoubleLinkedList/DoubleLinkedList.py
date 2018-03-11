from DataStructure.DoubleLinkedList.Node import CDLLNode

# Class double linked list
# Each node in the list is unique
class CDoubleLinkedList(object):
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        res = ""
        a = self.TraverseList()
        n = len(a)
        if n > 0:
            for i in range(0, n - 1, 1):
                res += str(int(a[i])) + ", "
            res += str(int(a[n-1]))
        return res

    def Exist(self, key):
        p = self.__head
        while p is not None:
            if p.GetKey() == key:
                return True
            else:
                p = p.GetNextNode()
        return False

    def Insert(self, key):
        if self.Exist(key) is True:
            return False
        if self.__head is None:
            self.__head = CDLLNode(key)
            self.__tail = self.__head
        else:
            p = CDLLNode(key)
            self.__tail.SetNextNode(p)
            p.SetPreviousNode(self.__tail)
            self.__tail = p
        return True

    def TraverseList(self):
        a = []
        p = self.__head
        while p is not None:
            a.append(p.GetKey())
            p = p.GetNextNode()
        return a

    def Remove(self, key):
        p = self.__head
        if p is None:
            return False
        if p.GetKey() == key:
            if p.GetNextNode() is None:
                self.__head = None
                self.__tail = None
                del p
            else:
                self.__head = p.GetNextNode()
                self.__head.SetPreviousNode(None)
                p.SetNextNode(None)
                del p
            return True
        else:
            p = p.GetNextNode()
            while p is not None:
                if p.GetKey() == key:
                    prev = p.GetPreviousNode()
                    next = p.GetNextNode()
                    prev.SetNextNode(next)
                    if next is not None:
                        next.SetPreviousNode(prev)
                    p.SetPreviousNode(None)
                    p.SetNextNode(None)
                    del p
                    return True
                else:
                    p = p.GetNextNode()
            return False
