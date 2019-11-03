"""
The International Standard Book Number (ISBN) is a unique commercial book
identifier. It is a string of length  10. The first 9 characters are digits; the
last character is a check character. The check character is the sum of the first
9 digits, mod 11, with 10 represented as 'X'. (Modern ISBNs use 13 digits, and
the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs.)

Create a cache for looking up prices of books identified by their ISBN. You
implement lookup, insert, and remove methods. Use the Least Recently Used (LRU)
policy for cache eviction. If an ISBN is already present, insert should not
change the price, but it should update that entry to be the most recently used
entry. Lookup should also update that entry to be the most recently used entry.

Hint: Amortize the cost of deletion. Alternatively, use an auxiliary data
structure.

"""

from collections import OrderedDict


class LRUCache:
    """
    Space complexity: O(n)
    Time complexity: O(1)

    """

    def __init__(self, capacity):
        self._isbn_price_table = OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price

    def insert(self, isbn, price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)
        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None
