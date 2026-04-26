from typing import List

DEFAULT_SIZE = 15


class Node:
    Pointer: int
    Value: any

    def __init__(self):
        self.Pointer = -1
        self.Value = None
    

class LinkedList:
    Array: List[Node]
    HeadPointer: int
    FreePointer: int

    def __init__(self):
        self.Array = [ Node() for _ in range(DEFAULT_SIZE) ]
        self.FreePointer = 0
        self.HeadPointer = -1

        for i in range( DEFAULT_SIZE - 1 ):
            self.Array[i].Pointer = i + 1

        self.Array[DEFAULT_SIZE - 1].Pointer = -1

    def Display(self):
        for i in self.Array:
            print(f"Value: {i.Value} | Pointer: {i.Pointer}")

    
    def GetInsertionPointer(self):
        if (self.HeadPointer == -1):
            return -1
        
        Pointer = self.HeadPointer

        while (self.Array[Pointer].Pointer != -1):
            Pointer = self.Array[Pointer].Pointer

        return Pointer
    
    def FindPointerOf(self, Value):
        if (self.HeadPointer == -1):
            return -1
        
        Pointer = self.HeadPointer

        while ( (Pointer != -1) and (self.Array[Pointer].Value != Value) ):
            Pointer = self.Array[Pointer].Pointer

        return Pointer



    def Append(self, Value):
        if (self.FreePointer == -1):
            return
        
        OldFreePointer = self.FreePointer
        NewFreePointer = self.Array[ OldFreePointer ].Pointer

        self.Array[ OldFreePointer ].Value = Value
        self.Array[ OldFreePointer ].Pointer = -1

        self.FreePointer = NewFreePointer


        if (self.HeadPointer == -1):
            self.HeadPointer = OldFreePointer
        else:
            InsertionPointer = self.GetInsertionPointer()

            self.Array[ InsertionPointer ].Pointer = OldFreePointer

    def Prepend(self, Value):
        if (self.FreePointer == -1):
            return
        
        OldFreePointer = self.FreePointer
        NewFreePointer = self.Array[OldFreePointer].Pointer

        self.Array[ OldFreePointer ].Value = Value
        self.Array[ OldFreePointer ].Pointer = -1

        self.FreePointer = NewFreePointer

        if (self.HeadPointer == -1):
            self.HeadPointer = OldFreePointer
        else:
            self.Array[ OldFreePointer ].Pointer = self.HeadPointer
            self.HeadPointer = OldFreePointer

    def Insert(self, Value, After):
        if (self.FreePointer == -1):
            return
        
        OldFreePointer = self.FreePointer
        FoundPointer = self.FindPointerOf( After )

        if ( FoundPointer != -1 ):
            self.Array[ OldFreePointer ].Value = Value

            self.FreePointer = self.Array[ OldFreePointer ].Pointer

            self.Array[ OldFreePointer ].Pointer = self.Array[ FoundPointer ].Pointer 
            self.Array[ FoundPointer ].Pointer = OldFreePointer



    def Delete(self, Value):
        if (self.HeadPointer == -1):
            return
        
        # Find Pointer that Points to Value
        # Find Pointer

        Pointer = self.FindPointerOf( Value )        

        if (Pointer != -1):
            PreviousPointer = self.HeadPointer
            
            if (Pointer == self.HeadPointer):
                # Deleting the HeadPointer
                self.HeadPointer = self.Array[Pointer].Pointer

                self.Array[Pointer].Value = None
                self.Array[Pointer].Pointer = -1

    
            else:

                while (self.Array[PreviousPointer].Pointer != Pointer):
                    PreviousPointer = self.Array[PreviousPointer].Pointer

        
                self.Array[ Pointer ].Value = None
                self.Array[ PreviousPointer ].Pointer = self.Array[ Pointer ].Pointer
                self.Array[ Pointer ].Pointer = -1

            
            self.FreePointer = Pointer
    
            
    def Output(self):
        if (self.HeadPointer == -1):
            return
        
        Pointer = self.HeadPointer

        while (Pointer != -1):
            print( self.Array[Pointer].Value )

            Pointer = self.Array[Pointer].Pointer

        
def Main():
    MyLinkedList = LinkedList()

    MyLinkedList.Append("Cat")
    MyLinkedList.Append("Dog")
    MyLinkedList.Append("Bat")
    
    MyLinkedList.Prepend("Manatee")
    MyLinkedList.Prepend("SeaLion")

    MyLinkedList.Insert("Seal", "Bat")

    MyLinkedList.Output()

    MyLinkedList.Delete("Seal")

    MyLinkedList.Output()

Main()