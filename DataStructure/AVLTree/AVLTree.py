from DataStructure.AVLTree.AVLNode import AVLNode

class AVLTree(object):
    # Constructor of the class
    def __init__(self):
        self.__root = None
        self.__size = 0

    # Print function of the class
    def __str__(self):
        res = ""
        array = self.GetArray()
        p = self.__root
        while p is not None:
            idx = self.__FindIdx(p.GetKey(), array)
            for i in range(0, idx, 1):
                res += '\t'
            res += str(p.GetKey())

    # Get total number of nodes in the tree
    def Size(self):
        return self.__size

    # To check whether a node respective to a given key exists in the tree or not
    def IsExistent(self, key):
        if self.__root is None:
            return False
        else:
            return self.__root.IsExistent(key)

    # To get the node respective to the given key
    def GetNode(self, key):
        if self.__root is None:
            return None
        return self.__root.GetNode(key)

    # Insert a new node into the tree
    # If the tree becomes unbalance, update it
    def Insert(self, key):
        if self.__root is None:
            self.__root = AVLNode(key)
            self.__size += 1
        else:
            p = self.__root.Insert(key)
            if p is not None:
                self.__root = p

    # Delete the node respective to the given key
    def Delete(self, key):
        pass

    # Array of all nodes' keys In-order
    def GetArrayInOrder(self):
        array = []
        if self.__root is not None:
            self.__root.TraverseInOrder(array)
        return array

    # Array of all nodes' keys Pre-order
    def GetArrayPreOrder(self):
        array = []
        if self.__root is not None:
            self.__root.TraversePreOrder(array)
        return array

    # Array of all nodes' keys Post-order
    def GetArrayPostOrder(self):
        array = []
        if self.__root is not None:
            self.__root.TraversePostOrder(array)
        return array

    def __FindIdx(self, key, array):
        n = len(array)
        for i in range(0, n, 1):
            if key == array[i]:
                return i
        return -1

    # Input is the list of parent nodes
    # Output is the list of children nodes
    def __GetALlChildren(self, parent):
        res = []
        n = len(parent)
        for i in range(0, n, 1):
            if parent[i].__left is not None:
                res.append(parent[i].__left)
            if parent[i].__right is not None:
                res.append(parent[i].__right)
        return res
