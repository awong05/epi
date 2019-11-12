"""
Designing a good spelling correction system can be challenging. We discussed
spelling correction in the context of edit distance (Problem 16.2 on Page 239).
However, in that problem, we only computed the Levenshtein distance between a
pair of strings. A spell checker must find a set of words that are closest to a
given word from an entire dictionary. Furthermore, the Levenshtein distance may
not be the right distance function when performing spelling correction—it does
not take into account the commonly misspelled words or the proximity of letters
on a keyboard.

How would you build a spelling correction system?

Hint: Start with an appropriate notion of distance between words.

"""

"""
The basic idea behind most spelling correction systems is that the misspelled
word's Levenshtein distance from the intended word tends to be very small (one
or two edits). Hence, if we keep a hash table for all the words in the
dictionary and look for all words that have a Levenshtein distance of 2 from the
text, it is likely that the intended word will be found in this set. If the
alphabet has m characters and the search text has n characters, we need to
perform O(n**2m**2) hash table lookups. More precisely, for a word of length n,
we can pick any two characters and change them to any other character in the
alphabet. The total number of ways of selecting any two characters is
n(n - 1)/2, and each character can be changed to one of (m - 1) other chars.
Therefore, the number of lookups is n(n - 1)(m - 1)**2/2.

The intersection of the set of all strings at a distance of two or less from a
word and the set of dictionary words may be large. It is important to provide a
ranked list of suggestions to the users, with the most likely candidates are at
the beginning of the list. There are several ways to achieve this:

- Typing errors model—often spelling mistakes are a result of typing errors.
Typing errors can be modeled on keyboard layouts.
- Phonetic modeling—a big class of spelling errors happen when the person
spelling it knows how the words sounds but does not know the exact spelling. In
such cases, it helps to map the text to phonemes aand then find all the words
that map to the same phonetic sequence.
- History of refinements—often users themselves provide a great amount of data
about the most likely misspellings by first entering a misspelled word and then
correcting it. This historic data is often immensely valuable for spelling
correction.
- Stemming—often the size of a dictionary can be reduced by keeping only the
stemmed version of each word. (This entails stemming the query text.)

"""
