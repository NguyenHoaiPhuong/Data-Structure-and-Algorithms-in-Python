# Double Linked List Node class
# There are 3 private properties:
# 1- key (type integer)
# 2- Left Node (type CDLLNode)
# 3- Right Node (type CDLLNode)
class CDLLNode(object):
    def __init__(self, key):
        self.__key = key
        self.__next = None
        self.__prev = None

    def __str__(self):
        strRes = "key = " + str(self.__key)
        if self.__prev is not None:
            strRes += ", previous key = " + str(self.__prev.__key)
        else:
            strRes += ", previous key = None"
        if self.__next is not None:
            strRes += ", next key = " + str(self.__next.__key)
        else:
            strRes += ", next key = None"
        return strRes

    def GetKey(self):
        return self.__key

    def SetKey(self, key):
        self.__key = key

    def GetNextNode(self):
        return self.__next

    def SetNextNode(self, next):
        self.__next = next

    def GetPreviousNode(self):
        return self.__prev

    def SetPreviousNode(self, prev):
        self.__prev = prev
