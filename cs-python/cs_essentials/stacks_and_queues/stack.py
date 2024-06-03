
class Node[T]:

    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

    def __str__(self) -> str:
        return str(self.value)



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

    def add(self, value: T):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> Node[T] | None:
        if self._head is None:
            return None

        node = self._head
        self._head = node.next

        return node
        

if __name__ == "__main__":
    print("Test Stack") 

    stack = Stack[int]()
    print(stack)

    stack.add(3)
    stack.add(1)
    stack.add(5)

    print(stack)
    
    for _ in range(3):
        print(f"Pop: {stack.pop()}")
        print(stack)

