from DataStructure.BinarySearchTree.Node import BSTNode

Mo = BSTNode()
Mo.SetData(20)
Mo.Insert(10)
Mo.Insert(30)
Mo.Insert(15)
Mo.Insert(100)
Mo.Insert(50)
Mo.Insert(200)
Mo.Insert(75)
Mo.Insert(115)

Mo.Remove(75)
Mo.Remove(115)
print("Tree Height:")
print(Mo.GetHeight())
a = Mo.TraverseTree()
print(a)

Ka = Mo.Find(30)
print(Ka)

Yu = Mo.FindMax()
print(Yu)

Ki = Mo.FindMin()
print(Ki)



