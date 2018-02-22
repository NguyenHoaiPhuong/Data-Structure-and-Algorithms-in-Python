
class BSTNode(object):
    def __init__(self, data = None):
        self.__data = data
        self.__left = None
        self.__right = None
        self.__parent = None

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

    def GetParent(self):
        return self.__parent

    def SetParent(self, parent):
        self.__parent = parent

    # Check whether the node is a leaf of a BST
    def IsLeaf(self):
        if self.__left is None and self.__right is None:
            return True
        else:
            return False

    # Insert a node whose value is data into the current tree.
    # If the data already exists, do not insert.
    def Insert(self, data):
        if data is None:
            return
        if self.__data is None:
            self.__data = data
        if data < self.__data:
            if self.__left is None:
                self.__left = BSTNode(data)
                self.__left.__parent = self
            else:
                self.__left.Insert(data)
        elif data > self.__data:
            if self.__right is None:
                self.__right = BSTNode(data)
                self.__right.__parent = self
            else:
                self.__right.Insert(data)

    # Remove the node whose value is data
    def Remove(self, data):
        if self is None:
            return
        if data < self.__data:
            self.__left.Remove(data)
        elif data > self.__data:
            self.__right.Remove(data)
        else:
            if self.__left is not None:
                p = self.__left
                while p.__right is not None:
                    p = p.__right
                self.__data = p.__data
                p.__parent.__right = None
                del p
            elif self.__right is not None:
                p = self.__right
                while p.__left is not None:
                    p = p.__left
                self.__data = p.__data
                p.__parent.__left = None
                del p
            else:
                if self.__parent is None:
                    del self
                else:
                    if self.__parent.__data > self.__data:
                        self.__parent.__left = None
                        del self
                    else:
                        self.__parent.__right = None
                        del self

    # Traverse the whole tree and store all node data into a list.
    def __TraverseTree(self, a):
        if self.__left is not None:
            self.__left.__TraverseTree(a)
        a.append(self.__data)
        if self.__right is not None:
            self.__right.__TraverseTree(a)

    def TraverseTree(self):
        a = []
        self.__TraverseTree(a)
        return a

    # Find the Node whose value is data
    def Find(self, data):
        if self is None:
            return None
        if data < self.__data:
            return self.__left.Find(data)
        elif data > self.__data:
            return self.__right.Find(data)
        else:
            return self

    # Find the node whose value is Max in the tree
    def FindMax(self):
        if self.__right is not None:
            return self.__right.FindMax()
        else:
            return self

    # Find the node whose value is Min in the tree
    def FindMin(self):
        if self.__left is not None:
            return self.__left.FindMin()
        else:
            return self

    # Get number of children of a node
    def GetNumberOfChild(self):
        res = 0
        if self.__left is not None:
            res += 1
        if self.__right is not None:
            res += 1
        return res

    # Get the height of the tree
    def GetHeight(self):
        if self is None:
            return 0
        else:
            if self.__left is None and self.__right is None:
                return 1
            elif self.__left is None and self.__right is not None:
                return 1 + self.__right.GetHeight()
            elif self.__left is not None and self.__right is None:
                return 1 + self.__left.GetHeight()
            else:
                MAX = max(self.__left.GetHeight(), self.__right.GetHeight())
                return MAX + 1