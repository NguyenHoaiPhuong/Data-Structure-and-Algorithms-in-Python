from DataStructure.BinarySearchTree.Node import BSTNode

def Find(array, val, s = None, e = None):
    if s is None and e is None:
        s = 0
        e = len(array) - 1
        return Find(array, val, s, e)
    else:
        if e == s:
            if array[s] != val:
                return -1
            else:
                return s
        elif e > s:
            m = int((s+e+1)/2)
            if val < array[m]:
                e = m-1
                return Find(array, val, s, e)
            elif val > array[m]:
                s = m
                return Find(array, val, s, e)
            else:
                return m

class BinaryTree(object):
    def __init__(self):
        self.__root = None
        self.__count = 0

    def __str__(self):
        res = ""
        array = self.__root.TraverseTree()
        a = self.__ClassifyNode()
        for i in range(0, len(a), 1):
            Idx = 0
            preIdx = 0
            for j in range(0, len(a[i]), 1):
                value = a[i][j].GetData()
                preIdx = Idx
                Idx = Find(array, value)
                tab = '\t'
                res += tab * (Idx - preIdx)
                res += str(value)
            res += '\n'
        return res

    # Total number of nodes in the binary tree
    def GetSize(self):
        return self.__count

    # The height of the tree
    def GetHeight(self):
        if self.__root is not None:
            return self.__root.GetHeight()
        else:
            return 0

    # Root Node
    def GetRoot(self):
        return self.__root

    # Insert new member into the tree
    def Insert(self, data):
        if self.__root is None:
            self.__root = BSTNode(data)
            self.__count += 1
        else:
            if self.__root.Insert(data) is True:
                self.__count += 1

    # Print Ascending Sorted Array
    def PrintInAscendingOrder(self):
        array = self.AscendingOrder()
        res = ""
        for i in range(0, len(array), 1):
            res += str(array[i])
            res += '\t'
        print(res)

    # Ascending order
    def AscendingOrder(self):
        return self.__root.TraverseTree()


    # Collect all nodes in the same level.
    # Level 1: the root node
    # Height of the the tree is the total number of level
    def __CollectNodeInNextLevel(self, a = []):
        res = []
        n = len(a)
        for i in range(0, n, 1):
            if a[i].GetLeftNode() is not None:
                res.append(a[i].GetLeftNode())
            if a[i].GetRightNode() is not None:
                res.append(a[i].GetRightNode())
        return res

    # Store nodes in the same level into 1 list
    # Store each level list into 1 list, which is called the Classified Binary Tree List
    def __ClassifyNode(self):
        res = []
        a = []
        if self.__root is not None:
            a.append(self.__root)
            res.append(a)
            bStop = False
            while bStop is False:
                a = self.__CollectNodeInNextLevel(a)
                if len(a) > 0:
                    res.append(a)
                else:
                    bStop = True
        return res
