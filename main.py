from Heap import KMinHeap
import random


# BiHeap = KMinHeap()


# BiHeap.Insert(13)
# BiHeap.Insert(14)
# BiHeap.Insert(16)
# BiHeap.Insert(19)
# BiHeap.Insert(21)
# BiHeap.Insert(19)
# BiHeap.Insert(68)
# BiHeap.Insert(65)
# BiHeap.Insert(26)
# BiHeap.Insert(32)
# BiHeap.Insert(31)

# BiHeap.Insert(12)
# BiHeap.Insert(11)
# BiHeap.Insert(13)
# BiHeap.Insert(14)
# BiHeap.Insert(15)
# BiHeap.Insert(18)
# BiHeap.Insert(10)

# print(BiHeap.Heap)

# BiHeap.Pop()

# print(BiHeap.Heap)

# BiHeap.Pop()

# print(BiHeap.Heap)

# BiHeap.Pop()

# print(BiHeap.Heap)

# BiHeap.Pop()

# print(BiHeap.Heap)

BiHeap = KMinHeap(2)

for i in [5, 7, 6, 9, 7, 6, 6, 15, 9, 12, 16, 17, 17, 14, 12, 17, 17, 16, 11, 16]:
    BiHeap.Insert(i)

print(BiHeap.Heap)
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Pop()
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Insert(20)
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))
BiHeap.Insert(1)
print(BiHeap.Heap)
print(BiHeap.Heap[0] == min(BiHeap.Heap))