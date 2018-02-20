from DataStructure.BinarySearchTree.Node import BSTNode

class BinaryTree(object):
    def __init__(self):
        self.__root = None

    def __str__(self):
        pass

    def Insert(self, data):
        if self.__root is None:
            self.__root = BSTNode(data)
        else:
            self.__root.Insert(data)
