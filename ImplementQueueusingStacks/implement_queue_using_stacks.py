class StackNode:
    def __init__(self, stored_value):
        self.stored_value = stored_value
        self.next_node = None

class LinkedStack:
    def __init__(self):
        self.top_node = None
        self.current_size = 0

    def push(self, value) -> None:
        new_node = StackNode(value)
        new_node.next_node = self.top_node
        self.top_node = new_node
        self.current_size += 1

    def pop(self):
        removed_value = self.top_node.stored_value
        self.top_node = self.top_node.next_node
        self.current_size -= 1
        return removed_value

    def peek(self):
        return self.top_node.stored_value

    def is_empty(self) -> bool:
        return self.current_size == 0

class MyQueue:
    def __init__(self):
        self.inbox_stack  = LinkedStack()
        self.outbox_stack = LinkedStack()

    def _lazy_transfer(self) -> None:
        if self.outbox_stack.is_empty():
            while not self.inbox_stack.is_empty():
                self.outbox_stack.push(self.inbox_stack.pop())

    def push(self, x: int) -> None:
        self.inbox_stack.push(x)

    def pop(self) -> int:
        self._lazy_transfer()
        return self.outbox_stack.pop()

    def peek(self) -> int:
        self._lazy_transfer()
        return self.outbox_stack.peek()

    def empty(self) -> bool:
        return self.inbox_stack.is_empty() and self.outbox_stack.is_empty()
