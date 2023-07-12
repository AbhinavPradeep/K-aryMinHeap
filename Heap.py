from Node import Node
import numpy as np
import sys
import math
np.set_printoptions(threshold=sys.maxsize)

class KMinHeap:
    def __init__(self,k=2) -> None:
        #Create a heap to accomidate 3 levels of a k-are tree
        # if k == 1:
        #     Size = 3
        # else:
        #     Size = int(((k**3)-1)/(k-1))
        self.k = k
        self.Heap = [None]
    
    def Insert(self, ValueToBeInserted) -> None:
        if self.Heap[0] == None:
            self.Heap[0] = ValueToBeInserted
        else:
            self.Heap.append(None)
            Index = len(self.Heap)-1
            # if self.Heap[Index] != None:
            #     NewSize = self.Resize()
            #     Index = NewSize-1
            # while self.Heap[Index] == None and self.Heap[Index-1] == None:
            #     Index = Index-1
            # if self.Heap[Index] == None and self.Heap[Index-1] != None:
            while Index != 0 and self.Heap[math.floor((Index-1)/self.k)] > ValueToBeInserted:
                self.Heap[Index] = self.Heap[math.floor((Index-1)/self.k)]
                Index = math.floor((Index-1)/self.k)

            self.Heap[Index] = ValueToBeInserted

    def Peek(self):
        return self.Heap[0]
    
    def Pop(self):
        Head = self.Heap[0]
        self.Heap[0] = None
        Index = 0
        while (Index*self.k)+1 <= (len(self.Heap)-1):
            Children = [self.Heap[(Index*self.k)+(i+1)] for i in range(self.k) if ((Index*self.k)+(i+1))<=(len(self.Heap)-1)]
            if self.Heap[-1] <= min(Children):
                break
            MinimumChild = min(Children)
            self.Heap[Index] = MinimumChild
            if Children.count(MinimumChild) > 1:
                Indices = [(Index*self.k)+(i+1) for i,Child in enumerate(Children) if Child == MinimumChild]
                ChildrensChildren = [self.Heap[(i*self.k)+(j+1)] for i in Indices for j in range(self.k) if ((i*self.k)+(j+1))<=(len(self.Heap)-1)]
                if ChildrensChildren == []:
                    Index = Children.index(MinimumChild)
                else:
                    MinimumChild = min(ChildrensChildren)
                    MinIndex = ChildrensChildren.index(MinimumChild)
                    IndexOfMinParent = math.ceil(MinIndex/self.k)-1
                    Index = Indices[IndexOfMinParent]
            else:
                IndexOfMinimumChild = Children.index(MinimumChild)
                Index = (Index*self.k)+(IndexOfMinimumChild+1)
        self.Heap[Index] = self.Heap[-1]
        self.Heap.pop(-1)
        return Head
    
    def Resize(self):
        NewSize = int(self.k*len(self.Heap))
        NewHeap = np.empty(NewSize,dtype=Node)
        for i,j in np.ndenumerate(self.Heap):
            NewHeap[i] = j
        self.Heap = NewHeap
        return NewSize