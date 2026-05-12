from random import randint
from typing import List


def InsertionSort( Arr: List ):
    n = len( Arr )

    for i in range(n): # Iterate through each element as normal.
        j = i

        # In insertion sort, each element is sorted individually.
        # As in, if I have the numbers { 6, 3, 5, 2, 8 }, let's say this array uses 0 as the first element
        # We start at 6. It's already at the start of the array, can't do much from here.
        # We move to 3. 3 is compared with 6, 3 is smaller than 6. Swap their indexes. {3, 6, 5, 2, 8}
        # We move to 5. 5 is smaller than 6. Swap their indexes. {3, 5, 6, 2, 8}.
        # We move to 2. 2 is smaller than 6. Swap their indexes. {3, 5, 2, 8}. 2 is smaller than 5. Swap. {3, 2, 5, 8}. 2 is smaller than 3. Swap. {2, 3, 5, 2, 8}. At the beginning the Array again, so we stop.
        # And the same process for the final element, 8.

        # The initial for loop is how we traverse to each value in the array.
        # The while loop is how we sort it.

        while ( j > 0 ):
            k = j - 1

            elemK = Arr[ k ] 
            elemJ = Arr[ j ]

            if ( elemK < elemJ ): # Change this to < to sort in descending order.
                break
            else:
                Arr[ j ] = elemK
                Arr[ k ] = elemJ

                j -= 1


def Q_InsertionSort( Arr: List ): # How the algorithm looks when writing it as short as possible.
    for i in range( len(Arr) ):
        j = i

        while ( (j > 0) and (Arr[j - 1] < Arr[j] ) ):
            Temp = Arr[j]

            Arr[j] = Arr[j - 1]
            Arr[j - 1] = Temp

            j -= 1


def Main():
    SampleArray = [ randint(0, 100) for _ in range(50) ]

    print( SampleArray )

    Q_InsertionSort( SampleArray )

    print( SampleArray ) 



Main()