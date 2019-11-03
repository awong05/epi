"""
Write a program which takes text for an anonymous letter and text for a magazine
for determines if it is possible to write the anonymous letter using the
magazine. The anonymous letter can be written using the magazine if for each
character in the anonymous letter, the number of times it appears in the
anonymous letter is no more than the number of times it appears in the magazine.

Hint: Count the number of distinct characters appearing in the letter.

"""

from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    """
    Space complexity: O(L)
    Time complexity: O(m + n)

    """

    char_frequency_for_letter = Counter(letter_text)

    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True

    return not char_frequency_for_letter


def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not (Counter(letter_text) - Counter(magazine_text))
