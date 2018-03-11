from DataStructure.DoubleLinkedList.DoubleLinkedList import CDoubleLinkedList

Akagi = CDoubleLinkedList()
Akagi.Insert(10)
Akagi.Insert(5)
Akagi.Insert(8)
Akagi.Insert(2)
Akagi.Insert(7)
Akagi.Insert(1)
Akagi.Insert(10)

Akagi.Remove(10)
Akagi.Remove(1)
Akagi.Remove(8)

print(Akagi)