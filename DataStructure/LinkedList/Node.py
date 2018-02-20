class LLNode(object):
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        Res = "Value = " + str(self.value) + ", Next Node is " + str(self.next)
        return Res

    def SetValue(self, value):
        self.value = value

    def GetValue(self):
        return self.value

    def SetNextNode(self, next):
        self.next = next

    def GetNextNode(self):
        return self.next