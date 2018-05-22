class AVLNode(object):
    # Constructor of the class
    def __init__(self, key, parent = None):
        self.__key = key
        self.__left = None
        self.__right = None
        self.__parent = parent
        self.__height = 0
        self.__balance = 0

    # Print function of the class
    def __str__(self):
        res = "key = " + str(self.__key)

        res += ", left = "
        if self.__left is not None:
            res += str(self.__left.__key)
        else:
            res += "None"

        res += ", right = "
        if self.__right is not None:
            res += str(self.__right.__key)
        else:
            res += "None"

        res += ", parent = "
        if self.__parent is not None:
            res += str(self.__parent.__key)
        else:
            res += "None"
        return res

    # Key
    def GetKey(self):
        return self.__key

    # Left Node
    def GetLeft(self):
        return self.__left
    def SetLeft(self, left):
        self.__left = left

    # Right Node
    def GetRight(self):
        return self.__right
    def SetRight(self, right):
        self.__right = right

    # Parent Node
    def GetParent(self):
        return self.__parent
    def SetParent(self, parent):
        self.__parent = parent

    # Height
    def GetHeight(self):
        return self.__height
    def SetHeight(self, height):
        self.__height = height

    # Balance
    def GetBalance(self):
        return self.__balance
    def SetBalance(self, balance):
        self.__balance = balance

    # To check whether a node with key value exists in the AVL tree or not
    def IsExistent(self, key):
        if key < self.__key:
            if self.__left is not None:
                return self.__left.IsExistent(key)
            else:
                return False
        elif key > self.__key:
            if self.__right  is not None:
                return self.__right.IsExistent(key)
            else:
                return False
        else:
            return True

    # To get the node with respective key
    def GetNode(self, key):
        if key == self.__key:
            return self
        elif key < self.__key:
            if self.__left is None:
                return None
            else:
                return self.__left.GetNode(key)
        else:
            if self.__right is None:
                return None
            else:
                return self.__right.GetNode(key)

    # Insert
    def Insert(self, key):
        if key < self.__key:
            if self.__left is not None:
                return self.__left.Insert(key)
            else:
                self.__left = AVLNode(key, self)
                p = self
                while p != None:
                    q = p.UpdateHeightAndBalance()
                    if q == None:
                        p = p.__parent
                    else:
                        if q.__parent is None:
                            return q
        elif key > self.__key:
            if self.__right is not None:
                return self.__right.Insert(key)
            else:
                self.__right = AVLNode(key, self)
                p = self
                while p != None:
                    q = p.UpdateHeightAndBalance()
                    if q == None:
                        p = p.__parent
                    else:
                        if q.__parent is None:
                            return q
        else:
            return None

    # After inserting or deleting a node, traverse up the tree and update the tree
    def UpdateHeightAndBalance(self):
        lH = -1
        rH = -1
        if self.__left is not None:
            lH = self.__left.__height
        if self.__right is not None:
            rH = self.__right.__height
        self.__height = max(lH, rH) + 1

        self.__balance = rH - lH
        if self.__balance == 2:
            if self.__right.__balance == 1:
                return self.RotateLeft()
            else:
                return self.RotateRightLeft()
        elif self.__balance == -2:
            if self.__left.__balance == -1:
                return self.RotateRight()
            else:
                return self.RotateLeftRight()
        return None

    #***************    Rotate Right     ***************#
    #               a                     x             #
    #             /  \                  /  \            #
    #           x     b               y     a           #
    #         /  \                  /     /  \          #
    #       y     c               z      c    b         #
    #     /                                             #
    #   z                                               #
    #***************************************************#
    def RotateRight(self):
        x = self.__left
        c = x.__right
        p = self.__parent
        if p is not None:
            if p.__left is self:
                p.__left = x
            else:
                p.__right = x
        x.__parent = p
        x.__right = self
        self.__parent = x
        self.__left = c
        if c is not None:
            c.__parent = self
        return x

    #***************    Rotate Left     ****************#
    #               a                     x             #
    #             /  \                  /  \            #
    #           b     x               a     y           #
    #               /  \            /  \     \          #
    #             c     y         b     c     z         #
    #                    \                              #
    #                     z                             #
    # **************************************************#
    def RotateLeft(self):
        p = self.__parent
        x = self.__right
        c = x.__left
        if p is not None:
            if p.__left is self:
                p.__left = x
            else:
                p.__right = x
        x.__parent = p
        x.__left = self
        self.__parent = x
        self.__right = c
        if c is not None:
            c.__parent = self
        return x

    # ***********************    Rotate Right Left     ************************#
    #               a                     a                          y         #
    #             /  \                  /  \                       /   \       #
    #           b     x     Rotate    b     y      Rotate        a      x      #
    #               /  \     Right        /  \      Left       /  \    / \     #
    #             y     c                z    x               b    z  T   c    #
    #           /  \                        /  \                               #
    #          z    T                      T    c                              #
    # *************************************************************************#
    def RotateRightLeft(self):
        self.__right.RotateRight()
        return self.RotateLeft()

    # ***********************    Rotate Left Right     ************************#
    #               a                     a                          y         #
    #             /  \                  /  \                       /   \       #
    #           x     b     Rotate    y     b      Rotate        x      a      #
    #         /  \           Left   /  \            Right      /  \    / \     #
    #       c     y               x     T                     c    z  T   b    #
    #           /  \            /  \                                           #
    #          z    T         c     z                                          #
    # *************************************************************************#
    def RotateLeftRight(self):
        self.__left.RotateLeft()
        return self.RotateRight()

    # Traverse along the tree following rule Left - Current - Right (In - Order)
    def TraverseInOrder(self, res = []):
        if self.__left is not None:
            self.__left.TraverseInOrder(res)
        res.append(self.__key)
        if self.__right is not None:
            self.__right.TraverseInOrder(res)

    # Traverse along the tree following rule Current - Left - Right (Pre-order)
    def TraversePreOrder(self, res = []):
        res.append(self.__key)
        if self.__left is not None:
            self.__left.TraversePreOrder(res)
        if self.__right is not None:
            self.__right.TraversePreOrder(res)

    # Traverse along the tree following rule Left - Right - Current (Post-order)
    def TraversePostOrder(self, res = []):
        if self.__left is not None:
            self.__left.TraversePostOrder(res)
        if self.__right is not None:
            self.__right.TraversePostOrder(res)
        res.append(self.__key)