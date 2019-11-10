"""
Spell checkers make suggestions for misspelled words. Given a misspelled string,
a spell checker should return words in the dictionary which are close to the
misspelled string.

In 1965, Vladimir Levenshtein defined the distance between two words as the
minimum number of "edits" it would take to transform the misspelled word into a
correct word, where a single edit is the insertion, deletion, or substitution of
a single character. For example, the Levenshtein distance between "Saturday" and
"Sundays" is 4—delete the first 'a' and 't', substitute 'r' by 'n' and insert
the trailing 's'.

Write a program that takes two strings and computes the minimum number of edits
needed to transform the first string into the second string.

Hint: Consider the same problem for prefixes of the two strings.

"""

def levenshtein_distance(A, B):
    """
    Space complexity: O(ab)
    Time complexity: O(ab)

    """

    def compute_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1
        elif B_idx < 0:
            return A_idx + 1
        if distance_between_prefixes[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[A_idx][B_idx] = (
                    compute_distance_between_prefixes(A_idx - 1, B_idx  - 1)
                )
            else:
                substitute_last = compute_distance_between_prefixes(
                    A_idx - 1, B_idx  - 1
                )
                add_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
                delete_last = compute_distance_between_prefixes(
                    A_idx, B_idx - 1
                )
                distance_between_prefixes[A_idx][B_idx] = (
                    1 + min(substitute_last, add_last, delete_last)
                )
        return distance_between_prefixes[A_idx][B_idx]

    distance_between_prefixes = [[-1] * len(B) for _ in A]
    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)
