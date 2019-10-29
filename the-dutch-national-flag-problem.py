"""
The quicksort algorithm for sorting arrays proceeds recursively—it selects an
element (the "pivot"), reorders the array to make all the elements less than or
equal to the pivot first, followed by all the elements greater than the pivot.
The two subarrays are then sorted recursively.

Implemented naively, quicksort has large run times and deep function call stacks
on arrays with many duplicates because the subarrays may differ greatly in size.
One solution is to reorder the array so that all elements less than the pivot
appear first, followed by elements equal to the pivot, followed by elements
greater than the pivot. This is known as Dutch national flag partitioning,
because the Dutch national flag consists of three horizontal bands, each in a
different color.

As an example, assuming that black precedes white and white precedes gray,
Figure 5.1(b) is a valid partitioning for Figure 5.1(a). If gray precedes black
and black precedes white, Figure 5.1(c) is a valid partitioning for Figure
5.1(a).

Generalizing, suppose A = <0,1,2,0,2,1,1>, and the pivot index is 3. Then A[3] =
0, so <0,0,1,2,2,1,1> is a valid partitioning. For the same array, if the pivot
index is 2, then A[2] = 2, so the arrays <0,1,0,1,1,2,2> as well as
<0,0,1,1,1,2,2> are valid partitionings.

Write a program that takes an array A and an index i into A, and rearranges the
elements such that all elements less than A[i] (the "pivot") appear first,
followed by elements equal to the pivot, followed by elements greater than the
pivot.

Hint: Think about the partition step in quicksort.

"""

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    """
    Space complexity: O(1)
    Time complexity: O(n**2)

    """

    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

def dutch_flag_partition(pivot_index, A):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    larager = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1

def dutch_flag_partition(pivot_index, A):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
