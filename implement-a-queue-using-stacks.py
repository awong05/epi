"""
Queue insertion and deletion follows first-in, first-out semantics; stack
insertion aand deletion is last-in, first-out.

How would you implement a queue given a library implementing stacks?

Hint: It is impossible to solve this problem with a single stack.

"""

class Queue:
    """
    Space complexity: O(n)
    Time complexity: O(m)

    """

    def __init__(self):
        self._enq, self._deq = [], []

    def enqueue(self, x):
        self._enq.append(x)

    def dequeue(self):
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())

        if not self._deq:
            raise IndexError('empty queue')
        return self._deq.pop()
