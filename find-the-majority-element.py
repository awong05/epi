"""
Several applications require identification of elements in a sequence which
occur more than a specified fraction of the total number of elements in the
sequence. For example, we may want to identify the users using excessive network
bandwidth or IP addresses originating the most Hypertext Transfer Protocol
(HTTP) requests. Here we consider a simplified version of this problem.

You are reading a sequence of strings. You know a priori that more than half the
strings are repetitions of a single string (the "majority element") but the
positions where the majority element occurs are unknown. Write a program that
makes a single pass over the sequence and identifies the majority element. For
example, if the input is <b,a,c,a,a,b,a,a,c,a>, then a is the majority element
(it appears in 6 out of the 10 places).

Hint: Take advantage of the existence of a majority element to perform
elimination.

NOTES:
- If the entry is different, we decrement the count.
- If the count becomes zero, we set the next entry to be the candidate.

"""

def majority_search(input_stream):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    candidate, candidate_count = None,  0
    for it in input_stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate ==  it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate
