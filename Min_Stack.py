from typing import Any

from MyStack import MyStack


class MinStack(MyStack):
    def __init__(self):
        super().__init__()
        self.min_stack = MyStack()

    def push(self, element=None) -> bool:
        if super().push(element):
            if self.min_stack.is_empty() or element < self.min_stack.peek():
                self.min_stack.push(element)
                return True
        return False

    def pop(self) -> Any:
        popped = super().pop()
        if popped == self.min_stack.peek():
            self.min_stack.pop()
        return popped

    def clear(self) -> None:
        super().clear()
        self.min_stack.clear()

    def get_min(self, a):
        self.min_stack.peek()


    def __str__(self):
        return self.stack.__str__()


def test(s):
    min_s = MinStack()
    for i in range(len(s)):
        min_s.push(s)

    print(min_s)


s = [1, 4, -8, 4, 7]
test(s)
