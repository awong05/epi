"""
People do not like reading text in which a word is used multiple times in a
short paragraph. You are to write a program which helps identify such a problem.

Write a program which takes as input an array and finds the distance between a
closest pair of equal entries. For example, if s = <"All","work","and","no",
"play","makes","for","no","work","no","fun","and","no","results">, then the
second and third occurrences of "no" is the closest pair.

Hint: Each entry in the array is a candidate.

"""

def find_nearest_repetition(paragraph):
    """
    Space complexity: O(d)
    Time complexity: O(n)

    """

    word_to_latest_index, nearest_repeated_distance = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(
                nearest_repeated_distance,
                i - latest_equal_word
            )
        word_to_latest_index[word] = i
    return nearest_repeated_distance \
        if nearest_repeated_distance != float('inf') else -1
