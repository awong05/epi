"""
When you type keywords in a search engine, the search engine will return
results, and each result contains a digest of the web page, i.e., a highlighting
within that page of the keywords that you searched for. For example, a search
for the keywords "Union" and "save" on a page with the text of the Emancipation
Proclamation should return the result shown in Figure 12.1.

The digest for this page is the text in boldface, with the keywords underlined
for emphasis. It is the shortest substring of the page which contains all the
keywords in the search. The problem of computing the digest is abstracted as
follows.

Write a program which takes an array of strings and a set of strings, and
returns the indices of the starting and ending index of a shortest subarray of
the given array that "covers" the set, i.e., contains all strings in the set.

Hint: What is the maximum number of minimal subarrays that cover the query?

NOTES:
- We can achieve a streaming algorithm by keeping track of latest occurrences of
query keywords as we process A.
- We use a doubly linked list L to store the last occurrence (index) of each
keyword in Q, and hash table H to map each keyword in Q to the corresponding
node in L.
- Each time a word in Q is encountered, we remove its node from L (which we find
by using H), create a new node which records the current index in A, and append
the new node to the end of L.

"""

from collections import Counter, namedtuple


Subarray = namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    """
    Space complexity: O(n)
    Time complexity: O(n)

    """

    keywords_to_cover = Counter(keywords)
    result = Subarray(-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[p1] += 1
                if keywords_to_cover[p1] > 0:
                    remaining_to_cover += 1
            left += 1
    return result

def find_smallest_subarray_covering_subset(stream, query_strings):
    """
    Space complexity: O(n)
    Time complexity: O(n)

    """

    class DoublyLinkedListNode:
        def __init__(self, data=None):
            self.data = data
            self.next = self.prev = None

    class LinkedList:
        def __init__(self):
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def insert_after(self, value):
            node = DoublyLinkedListNode(value)
            node.prev = self.tail
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self._size += 1

        def remove(self, node):
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            node.next = node.prev = None
            self._size -= 1

    loc = LinkedList()
    d = {s: None for s in query_strings}
    result = Subarray(-1, -1)
    for idx, s in enumerate(stream):
        if s in d:
            it = d[s]
            if it is not None:
                loc.remove(it)
            loc.insert_after(idx)
            d[s] = loc.tail

            if len(loc) == len(query_strings):
                if (result == (-1, -1) or \
                    idx - loc.head.data < result[1] - result[0]):
                    result = (loc.head.data, idx)
    return result
