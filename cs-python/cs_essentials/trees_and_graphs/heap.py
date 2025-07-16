from typing import NamedTuple


class Node(NamedTuple):
    parent: "Node"
    children: list["Node"]


class MinHeap[T: (int, float)]:
    """Min Heap"""

    def __init__(self) -> None:
        self._array: list[T] = []

    @classmethod
    def parent_idx(cls, i: int) -> int:
        return (i-1) // 2

    @classmethod
    def left_child_idx(cls, i: int) -> int:
        return 2 * i + 1

    @classmethod
    def right_child_ix(cls, i: int) -> int:
        return 2 * i + 2

    def insert(self, v: T) -> None:
        self._array.append(v)
        idx = len(self._array) - 1
        parent_idx = MinHeap.parent_idx(idx)
        while parent_idx >= 0:
            parent_value = self._array[parent_idx]
            if parent_value <= v:
                break
            self._swap(idx, parent_idx)
            idx = parent_idx
            parent_idx = MinHeap.parent_idx(idx)

    def extract_min(self) -> T | None:
        if not self._array:
            return None

        min_ = self._array[0]

        last_idx = len(self._array) - 1
        self._array[0] = self._array[last_idx]
        self._array.pop()
        last_idx -= 1

        idx = 0
        while True:
            right_child_idx = MinHeap.right_child_ix(idx)
            left_child_idx = MinHeap.left_child_idx(idx)
            if right_child_idx > last_idx:
                if left_child_idx > last_idx:
                    break
                target_idx = left_child_idx
            elif self._array[left_child_idx] <= self._array[right_child_idx]:
                target_idx = left_child_idx
            else:
                target_idx = right_child_idx
            
            if self._array[target_idx] >= self._array[idx]:
                break
            
            self._swap(idx, target_idx)
            idx = target_idx

        return min_

    
    def _swap(self, i: int, j: int) -> None:
        h = self._array[i]
        self._array[i] = self._array[j]
        self._array[j] = h
