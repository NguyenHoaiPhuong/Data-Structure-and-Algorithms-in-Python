
class BSTNode(object):
    def __init__(self, data = None):
        self.__data = data
        self.__left = None
        self.__right = None

    def __str__(self):
        res = "data = " + str(self.__data)
        if self.__left is not None:
            res += ", left node data = " + str(self.__left.__data)
        if self.__right is not None:
            res += ", right node data = " + str(self.__right.__data)
        return res

    def GetData(self):
        return self.__data

    def SetData(self, data):
        self.__data = data

    def GetLeftNode(self):
        return self.__left

    def SetLeftNode(self, left):
        self.__left = left

    def GetRightNode(self):
        return self.__right

    def SetRightNode(self, right):
        self.__right = right

    def IsLeaf(self):
        if self.__left is None and self.__right is None:
            return True
        else:
            return False

    def Insert(self, data):
        if data is None:
            return
        if self.__data is None:
            self.__data = data
        if data < self.__data:
            if self.__left is None:
                self.__left = BSTNode(data)
            else:
                self.__left.Insert(data)
        elif data > self.__data:
            if self.__right is None:
                self.__right = BSTNode(data)
            else:
                self.__right.Insert(data)

    def Remove(self, data):
        if self is None:
            return
        if data < self.__data:
            self.__left.Remove(data)
        elif data > self.__data:
            self.__right.Remove(data)
        else:
            if self.__left is not None:
                pass
            elif self.__right is not None:
                pass
            else:
                del self

    def __RemoveMax(self):
        if self.__right is not None:
            self.__right.__RemoveMax()
        else:
            pass

    def TraverseTree(self, a = []):
        if self.__left is not None:
            self.__left.TraverseTree()
        a.append(self.__data)
        if self.__right is not None:
            self.__right.TraverseTree()
        return a

    def Find(self, data):
        if self is None:
            return None
        if data < self.__data:
            return self.__left.Find(data)
        elif data > self.__data:
            return self.__right.Find(data)
        else:
            return self

    def FindMax(self):
        if self.__right is not None:
            return self.__right.FindMax()
        else:
            return self

    def FindMin(self):
        if self.__left is not None:
            return self.__left.FindMin()
        else:
            return self