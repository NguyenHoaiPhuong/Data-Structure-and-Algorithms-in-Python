from DataStructure.AVLTree.AVLTree import AVLTree

Akagi = AVLTree()
Akagi.Insert(10)
Akagi.Insert(20)
Akagi.Insert(25)
Akagi.Insert(35)

a = Akagi.GetArrayPreOrder()
print(a)

a = Akagi.GetArrayInOrder()
print(a)

a = Akagi.GetArrayPostOrder()
print(a)