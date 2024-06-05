
class Node[T]:

    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

    def __str__(self) -> str:
        return str(self.value)

class EmptyStackException(Exception):
    ...


class Stack[T]:

    def __init__(self):
        self._head: Node[T] | None = None

    def __str__(self) -> str:
        s = "["
        if self._head is None:
            return s + "]"
        
        node = self._head
        while node.next is not None:
            s += f"{node}, "
            node = node.next

        return s + f"{node}]"

    def push(self, value: T):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> Node[T]:
        if self._head is None:
            raise EmptyStackException

        node = self._head
        self._head = node.next

        return node

    def peek(self) -> Node[T]:
        if self._head is None:
            raise EmptyStackException

        return self._head


    def is_empty(self) -> bool:
        return self._head is None
        

if __name__ == "__main__":
    print("Test Stack") 

    stack = Stack[int]()
    stack.peek()
    print(stack)

    stack.push(3)
    stack.push(1)
    stack.push(5)

    print(stack)
    
    for _ in range(3):
        print(f"Pop: {stack.pop()}")
        print(stack)

