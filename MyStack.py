from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, element=None) -> bool:
        """Push an element onto the stack.

        Args:
            element: The element to be pushed onto the stack.

        Returns:
            bool: True if the element was successfully pushed, False otherwise.
        """
        if element is not None:
            self.stack.append(element)
            return True
        return False

    def pop(self) -> Any:
        """Remove and return the top element from the stack.

        Returns:
            Any: The top element of the stack.
        """
        if not self.is_empty():
            return self.stack.pop()

    def peek(self) -> Any:
        """Return the top element from the stack without removing it.

        Returns:
            Any: The top element of the stack.
        """

        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        if len(self.stack) > 0:
            return False
        return True

    def size(self) -> int:
        """Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self.stack.clear()


def func(S):
    stack = MyStack()
    a = "("
    b = "["
    c = "{"
    a_a = ")"
    b_b = "]"
    c_c = "}"
    if len(S) > 0:
        for i in range(len(S)):
            # if S[i] in ('{', ...)
            if S[i] == "(" or S[i] == "[" or S[i] == "{":
                stack.push(S[i])
            elif S[i] == a_a:
                if stack.peek() == a:
                    stack.pop()
                else:
                    return False
            elif S[i] == b_b:
                if stack.peek() == b:
                    stack.pop()
                else:
                    return False
            elif S[i] == c_c:
                if stack.peek() == c:
                    stack.pop()
                else:
                    return False
        return stack.is_empty()
    return stack.is_empty()


def test(func):
    legals = ['(()[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[][()]]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']
    illegal = ['}}))[{)({]',
               '{)({([)){}',
               '{{}[((]}}]',
               '[){{{{{)}(',
               '{}[[}]}(]{',
               '}[]]{[})[{',
               '][[([}[)()',
               '[)(]){]}(]',
               '(]}}[)})]]',
               '[)((])]{(}']
    for s in legals:
        assert func(s), s
    for s in illegal:
        assert not func(s), s
    print(True)


test(func)
