"""
Each digit, apart from 0 and 1, in a phone keypad corresponds to one of three or
four letters of the alphabet, as shown in Figure 6.1. Since words are easier to
remember than numbers,  it is natural to ask if a 7 or 10-digit phone number can
be represented by a word. For example, "2276696" corresponds to "ACRONYM" as
well as "ABPOMZN".

Write a program which takes as input a phone number, specified as a string of
digits, and returns all possible character sequences that correspond to the
phone number. The cell phone keypad is specified by a mapping that takes a digit
and returns the corresponding set of characters. The character sequences do not
have to be legal words or phrases.

Hint: Use recursion.

"""

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):
    """
    Time complexity: O(4**n(n))

    """

    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)

     mnemonics, partial_mnemonic = [], [0] * len(phone_number)
     phone_mnemonic_helper(0)
     return mnemonics
