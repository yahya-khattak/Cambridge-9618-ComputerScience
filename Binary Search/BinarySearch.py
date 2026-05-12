from typing import List


# For the A2 paper, you would be given the size of the array anyways. You could just pass it in as a parameter to the function.

def BinarySearch( Arr: List, element: any ):
    start = 0
    end = len( Arr ) - 1
    
    # Arrays in Python begin at index 0
    # Final index is size of the array - 1

    k = int ( ( start + end ) / 2 )  # Midpoint between two points. Convert to Integer to round DOWN

    if ( Arr[k] == element ): # if we already find what we're looking for here, great! no need to loop
        return k
    
    while ( start < end ): # Keep looping until the search space becomes 0.
        k = int( ( start + end ) / 2 )

        if ( Arr[k] == element ): # We have found the element we are looking for. Exit the loop, and return the index.
            return k

        if ( element > Arr[k] ):
            start = k + 1
        else:
            end = k - 1

    return -1 # could not find the element. Return a value to indicate that.


# Binary Search only worked on data that is already sorted.
# It assumes that if the value is looking for is greater, then it must lay in the upper half of the array.


def Main():
    print("Testing")

    SampleArray = sorted( [ int(10), int(20), int(30), int(40), int(50) ] )


    print( BinarySearch( SampleArray, 40 ) )


Main()