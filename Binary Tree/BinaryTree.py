DEFAULT_SIZE = 10


class Node:
    def __init__(self):
        self.LeftPointer = -1
        self.RightPointer = -1
        self.Value = None

class BinaryTree:
    def __init__(self):
        self.RootPointer = -1
        self.FreePointer = 0
        self.Array = [ Node() for _ in range( DEFAULT_SIZE ) ]

        # The array has to be initialized as a linked list whenever a constructor is called.
        # 
        # { 
        # [0] = { LeftPointer: 1, Value: None, RightPointer: -1 }
        # [1] = { LeftPointer: 2, Value: None, RightPointer: -1 }
        # ... and so on. LeftPointer, on initialization, points to the index of the next element in the Array.
        # The last element will have LeftPointer set to -1, to indicate that the Array ends.
        # }

        for i in range( DEFAULT_SIZE - 1 ):
            CurrentNode = self.Array[ i ]

            CurrentNode.LeftPointer = i + 1
        

        self.Array[ DEFAULT_SIZE - 1 ].LeftPointer = -1

    def GetInsertionPointer(self, Data):
        # Binary search through the tree

        Pointer = -1
        CurrentPointer = self.RootPointer
        IsLeft = False

        while (CurrentPointer != -1):
            Pointer = CurrentPointer

            CurrentValue = self.Array[ CurrentPointer ].Value

            if (Data < CurrentValue):
                IsLeft = True
                CurrentPointer = self.Array[ CurrentPointer ].LeftPointer
            else:
                IsLeft = False
                CurrentPointer = self.Array[ CurrentPointer ].RightPointer

        return Pointer, IsLeft;

    def Insert(self, Data):
        if (self.FreePointer == -1):
            # Binary Tree is full
            return
        
        CurrentPointer = self.FreePointer

        FreeNode = self.Array[self.FreePointer]

        FreeNode.Value = Data

        self.FreePointer = FreeNode.LeftPointer # Assign FreePointer to the next index before resetting this attribute
        
        FreeNode.LeftPointer = -1 # Reset this as it's no longer linked. This will be updated.

        if (self.RootPointer == -1):
            self.RootPointer = CurrentPointer
        else:
            UpdatedPointer, IsLeft = self.GetInsertionPointer( Data )

            if (UpdatedPointer != -1):

                if (IsLeft):
                    self.Array[UpdatedPointer].LeftPointer = CurrentPointer
                else:
                    self.Array[UpdatedPointer].RightPointer = CurrentPointer

        
    def Search(self, Data): # Returns -1 if not found, returns the pointer if found.
        Pointer = self.RootPointer

        while ( (Pointer != -1) ):
            CurrentNode = self.Array[ Pointer ]

            if ( Data == CurrentNode.Value ):
                return Pointer
            

            if (Data < CurrentNode.Value):
                Pointer = CurrentNode.LeftPointer
            else:
                Pointer = CurrentNode.RightPointer

    def Display(self):
        for i in self.Array:
            OutputString = f"LeftPointer: {i.LeftPointer} | Value: {i.Value} | RightPointer: {i.RightPointer}"

            print( OutputString )

    def Traverse(self, Pointer = 0):
        if (self.RootPointer == -1):
            return # Tree Empty
        
        CurrentNode = self.Array[ Pointer ]

        if (CurrentNode.LeftPointer != -1):
            self.Traverse( CurrentNode.LeftPointer )
        
        print( CurrentNode.Value )

        if (CurrentNode.RightPointer != -1):
            self.Traverse( CurrentNode.RightPointer )






def Main():
    MyTree = BinaryTree()

    MyTree.Insert("C")
    MyTree.Insert("A")
    MyTree.Insert("D")
    MyTree.Insert("F")
    MyTree.Insert("Z") 


    MyTree.Display()
    MyTree.Traverse()

    print( MyTree.Search("D") )

Main()