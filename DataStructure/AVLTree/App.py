from DataStructure.AVLTree.AVLTree import AVLTree

Akagi = AVLTree()

print("-------------------- Insert 50 -----------------------")
Akagi.Insert(50)
print(Akagi)

print("-------------------- Insert 30 -----------------------")
Akagi.Insert(30)
print(Akagi)

print("-------------------- Insert 10 -----------------------")
Akagi.Insert(10)
print(Akagi)

print("-------------------- Insert 6 ------------------------")
Akagi.Insert(6)
print(Akagi)

print("-------------------- Insert 20 -----------------------")
Akagi.Insert(20)
print(Akagi)

print("-------------------- Insert 21 -----------------------")
Akagi.Insert(21)
print(Akagi)

print("-------------------- Insert 25 -----------------------")
Akagi.Insert(25)
print(Akagi)

print("-------------------- Insert 28 -----------------------")
Akagi.Insert(28)
print(Akagi)

print("-------------------- Insert 12 -----------------------")
Akagi.Insert(12)
print(Akagi)

print("-------------------- Insert 17 -----------------------")
Akagi.Insert(17)
print(Akagi)

print("-------------------- Remove 30 -----------------------")
Akagi.Remove(30)
print(Akagi)

print("-------------------- Remove 50 -----------------------")
Akagi.Remove(50)
print(Akagi)

print("-------------------- Remove 20 -----------------------")
Akagi.Remove(20)
print(Akagi)

print("-------------------- Remove 6 ------------------------")
Akagi.Remove(6)
print(Akagi)

print("-------------------- Remove 10 -----------------------")
Akagi.Remove(10)
print(Akagi)

print("-------------------- Remove 2 -----------------------")
Akagi.Remove(2)
print(Akagi)

print("-------------------- Pre-order -----------------------")
a = Akagi.GetArrayPreOrder()
print(a)

print("-------------------- In-order -----------------------")
a = Akagi.GetArrayInOrder()
print(a)

print("-------------------- Post-order -----------------------")
a = Akagi.GetArrayPostOrder()
print(a)

print("----------------------------------")
print(Akagi)
print(Akagi.Size())
print(Akagi.GetHeight(30))
print(Akagi.GetBalance(30))
print(Akagi.GetNode(50))