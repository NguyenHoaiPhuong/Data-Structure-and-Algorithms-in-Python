class CNode(object):
    def __init__(self, value = None, next = None):
        self.__value = value
        self.__next = next

    def __str__(self):
        Res = "Value = " + str(self.__value) + ", Next Node is " + str(self.__next)
        return Res

    def SetValue(self, value):
        self.__value = value

    def GetValue(self):
        return self.__value

    def SetNextNode(self, next):
        self.__next = next

    def GetNextNode(self):
        return self.__next