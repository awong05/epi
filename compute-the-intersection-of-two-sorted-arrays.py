"""
A natural implementation for a search engine is to retrieve documents that match
the set of words in a query by maintaining an inverted index. Each page is
assigned an integer identifier, its document-ID. An inverted index is a mapping
that takes a word w and returns a sorted array of page-ids which contain w—the
sort order could be, for example, the page rank in descending order. When a
query contains multiple words, the search engine finds the sorted array for each
word and then computes the intersection of these arrays—these are the pages
containing all the words in the query. The most computationally intensive step
of doing this is finding the intersection of the sorted arrays.

Write a program which takes as input two sorted arrays, and returns a new sorted
array containing elements that are present in both of the input arrays. The
input arrays may have duplicate entries, but the returned array should be free
of duplicates. For example, the input is <2,3,3,5,5,6,7,7,8,12> and
<5,5,6,8,8,9,10,10>, your output should be <5,6,8>.

Hint: Solve the problem if the input array lengths differ by orders of
magnitude. What if they are approximately equal?

"""

def intersection_two_sorted_arrays(A, B):
    """
    Space complexity: O(1)
    Time complexity: O(m + n)

    """

    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B
