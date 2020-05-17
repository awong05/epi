"""
Consider the problem of laying out text using a fixed width front. Each line can
hold no more than a fixed number of characters. Words on a line are to be
separated by exactly one blank. Therefore, we may be left with whitespace at the
end of a line (since the next word will not fit in the remaining space). This
whitespace is visually unappealing.

Define the _messiness_ of the end-of-line whitespace as follows. The messiness
of a single line ending with b blank characters is b**2. The total messiness of
a sequence of lines is the sum of the messinesses of all the lines. A sequence
of words can be split across lines in different ways with different messiness,
as illustrated in Figure 16.12 on the next page.

Given text, i.e., a string of words separated by single blanks, decompose the
text into lines such that no word is split across lines and the messiness of the
decomposition is minimized. Each line can hold no more than a specific number of
characters.

Hint: Focus on the last word and the last line.

"""

def minimum_messiness(words, line_length):
    """
    Space complexity: O(n)
    Time complexity: O(nL)

    """

    num_remaining_blanks = line_length - len(words[0])
    min_messiness = ([num_remaining_blanks**2] + [float('inf')] *
                     (len(words) - 1))
    for i in range(1, len(words)):
        num_remaining_blanks = line_length - len(words[i])
        min_messiness[i] = min_messiness[i - 1] + num_remaining_blanks**2
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1
            if num_remaining_blanks < 0:
                break
            first_j_messiness = 0 if j - 1 < 0 else min_messiness[j - 1]
            current_line_messiness = num_remaining_blanks**2
            min_messiness[i] = min(min_messiness[i],
                                   first_j_messiness + current_line_messiness)
    return min_messiness[-1]
