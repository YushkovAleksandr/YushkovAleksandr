"""
Class stack implementation
"""

class Stack:
     def __init__(self):
         self._stack = []
         self.max = None
     def take(self):
         a=self._stack[len(self._stack)-1]
         self._stack=self._stack[:len(self._stack)-1]
         return a
     def push(self, item):
         self._stack.append(item)
         if len(self.stack) == 1 or item > self.max:
             self.max = item
     def lenght(self):
         return len(self._stack)