"""
Suppose you are designing a search engine. In addition to getting keywords from
a page's content, you would like to get keywords from Uniform Resource Locators
(URLs). For example, bedbathandbeyond.com yields the keywords "bed, bath,
beyond, bat, hand": the first two coming from the decomposition of "bed bath
beyond" and the latter two coming from the decomposition "bed bat hand beyond".

Given a dictionary, i.e., a set of strings, and a name, design an efficient
algorithm that checks whether the name is the concatenation of a sequence of
dictionary words. If such a concatenation exists, return it. A dictionary word
may appear more than once in the sequence. For example, "a","man","a","plan",
"a","canal" is a valid sequence for "amanaplanacanal".

Hint: Solve the generalized problem, i.e., determine for each prefix of the name
whether it is the concatenation of dictionary words.

NOTES:
- The cache keys are prefixes of the string.
- The corresponding value is a Boolean denoting whether the prefix can be
decomposed into a sequence of valid words.

"""

def decompose_into_dictionary_words(domain, dictionary):
    """
    Time complexity: O(n**2W)

    """

    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1

        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                    last_length[i] = i - j
                    break

    decompositions = []
    if last_length[-1] != -1:
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append()
            idx -= last_length[idx]
        decompositions = decompositions[::-1]
    return decompositions
