from DataStructure.AVLTree.AVLTree import AVLTree

Akagi = AVLTree()
Akagi.Insert(50)
Akagi.Insert(30)
Akagi.Insert(10)
Akagi.Insert(6)
Akagi.Insert(20)
Akagi.Insert(2)
Akagi.Remove(30)
Akagi.Remove(50)
Akagi.Remove(20)
#Akagi.Remove(6)
#Akagi.Remove(10)
#Akagi.Remove(2)

a = Akagi.GetArrayPreOrder()
print(a)

a = Akagi.GetArrayInOrder()
print(a)

a = Akagi.GetArrayPostOrder()
print(a)

print("----------------------------------")
print(Akagi)
print(Akagi.Size())
print(Akagi.GetHeight(30))
print(Akagi.GetBalance(30))
print(Akagi.GetNode(50))