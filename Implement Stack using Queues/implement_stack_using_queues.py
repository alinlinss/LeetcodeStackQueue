class QueueNode:
    def __init__(self, stored_value):
        self.stored_value = stored_value
        self.next_node = None

class LinkedQueue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.current_size = 0

    def enqueue(self, value) -> None:
        new_node = QueueNode(value)
        if self.rear_node is not None:
            self.rear_node.next_node = new_node
        self.rear_node = new_node
        if self.front_node is None:
            self.front_node = new_node
        self.current_size += 1

    def dequeue(self):
        removed_value = self.front_node.stored_value
        self.front_node = self.front_node.next_node
        if self.front_node is None:
            self.rear_node = None
        self.current_size -= 1
        return removed_value

    def peek_front(self):
        return self.front_node.stored_value

    def is_empty(self) -> bool:
        return self.current_size == 0

    def size(self) -> int:
        return self.current_size

class MyStack:
    def __init__(self):
        self.main_queue = LinkedQueue()

    def push(self, x: int) -> None:
        self.main_queue.enqueue(x)

        number_of_rotations = self.main_queue.size() - 1
        for _ in range(number_of_rotations):
            front_value = self.main_queue.dequeue()
            self.main_queue.enqueue(front_value)

    def pop(self) -> int:
        return self.main_queue.dequeue()

    def top(self) -> int:
        return self.main_queue.peek_front()

    def empty(self) -> bool:
        return self.main_queue.is_empty()
