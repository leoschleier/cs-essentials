import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[3].resolve()))

from cs_essentials.linked_list import LinkedList, Node 


def get_kth_to_last[T](l: LinkedList[T], k: int) -> Node[T]:
    if l.head is None:
        raise ValueError("List is empty.")
    if k < 1:
        raise ValueError("k must be > 0")
    
    counter = 1
    kth = node = l.head
    while node.next is not None:
        if counter == k:
            break

        node = node.next
        counter += 1

    if counter < k:
        raise ValueError("Not enough elements in list.")

    while node.next is not None:
        if kth.next is None:
            # This should never happen but the type checker cannot
            # infer that.
            raise Exception("kth.next is None.")
        node = node.next
        kth = kth.next

    return kth


if __name__ == '__main__':
    l = LinkedList[int]()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.append(7)
    l.append(8)
    l.append(9)
    l.append(10)

    print(l)
    print(get_kth_to_last(l, 3))
