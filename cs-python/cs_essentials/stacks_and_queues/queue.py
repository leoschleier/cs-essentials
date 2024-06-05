
class Item[T]:

    def __init__(self, value: T):
        self.value: T = value
        self.next: Item[T] | None = None

    def __str__(self) -> str:
        return str(self.value)


class EmptyQueueException(Exception):
    ...


class Queue[T]:

    def __init__(self):
        self._first: Item[T] | None = None
        self._last: Item[T] | None = None
        
    def __str__(self) -> str:
        if self._first is None:
            return "[]"
        

        item = self._first
        q = f"{item}"
        item = item.next
        while item is not None:
            q = f"{item}, {q}"
            item = item.next

        return f"[{q}]"
        

    def add(self, value: T):
        if self._last is None:
            self._first = self._last = Item(value)
            return
        
        item = Item(value)
        self._last.next = item 
        self._last = item 

    def remove(self) -> Item[T]:
        if self._first is None:
            raise EmptyQueueException

        item = self._first
        self._first = item.next

        return item

    def peek(self) -> Item[T]:
        if self._first is None:
            raise EmptyQueueException

        return self._first

    def is_empty(self) -> bool:
        return self._first is None


if __name__ == "__main__":
    print("Test queue")
    
    queue = Queue[int]()
    print(queue)

    queue.add(3)
    print(queue)
   
    queue.add(1)
    print(queue)
    
    queue.add(5)
    print(queue)

    queue.remove()
    print(queue)
    queue.remove()
    print(queue)
    queue.remove()
    print(queue)

