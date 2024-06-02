
class Node[T]:

    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] | None = None

class LinkedList[T]:

    def __init__(self):
        self._head: Node[T] | None = None
    
    def __str__(self) -> str:
        node = self._head
        if node is None:
            return str(None)
        
        ll = "["

        while node.next is not None:
            ll += f"{node.value}, "
            node = node.next
        
        ll += f"{node.value}]"
        return ll

    
    def append(self, value: T) -> None:
        new_node = Node(value)
        node = self._head

        if node is None:
            self._head = new_node
            return

        while node.next is not None:
            node = node.next

        node.next = new_node

    def remove(self, value: T) -> Node[T] | None:
        node = self._head

        if node is None:
            return node
        elif node.value == value:
            self._head = node.next
            return node

        while node.next is not None:
            next = node.next
            if next.value == value:
                node.next = next.next
                return next
            
            node = next

        return None


if __name__ == "__main__":
    print("Test Linked List")
    
    ll = LinkedList[int]()

    ll.append(3)
    print(ll)

    ll.append(5)
    print(ll)

    ll.append(1)
    print(ll)

    ll.remove(5)
    print(ll)

    ll.remove(1)
    print(ll)



