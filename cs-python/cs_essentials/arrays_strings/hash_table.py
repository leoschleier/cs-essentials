from typing import TYPE_CHECKING, Any, Self, SupportsBytes

if TYPE_CHECKING:
    from collections.abc import Generator


_FNV_OFFSET_BASIS = 14695981039346656037
_FNV_PRIME = 1099511628211
_LBS_MASK = 2**64 - 1

type _K = SupportsBytes
type _V = Any


class Head[_K, _V]:
    def __init__(self: Self) -> None:
        self.next: Node[_K, _V] | None = None


class Node[_K, _V]:
    def __init__(self: Self, key: _K, value: _V) -> None:
        self.next: Node[_K, _V] | None = None
        self._key = key
        self.value = value

    @property
    def key(self: Self) -> _K:
        return self._key

    def iter(self: Self) -> "Generator[Node[_K, _V], None, None]":
        next = self
        while next is not None:
            yield next
            next = self.next


class HashTable[_K, _V]:
    def __init__(self: Self, length: int) -> None:
        self._arr = tuple(Head[_K, _V]() for _ in range(length))
        self._table_len = length

    def set(self: Self, key: _K, value: _V) -> None:
        index = self._get_index(key)
        head = tail = self._arr[index]

        if ll := head.next:
            for node in ll.iter():
                tail = node
                if node.key == key:
                    node.value = value
                    return
        tail.next = Node(key, value)

    def get(self: Self, key: _K) -> _V:
        index = self._get_index(key)
        head = self._arr[index]
        if ll := head.next:
            for node in ll.iter():
                if node.key == key:
                    return node.value

        msg = f"Key {key} not found."
        raise KeyError(msg)

    def _get_index(self: Self, key: _K) -> int:
        return _fnv_1(bytes(str(key), "utf-8")) % self._table_len


def _fnv_1(bytes_: bytes) -> int:
    hash_ = _FNV_OFFSET_BASIS
    for b in bytes_:
        hash_ = (hash_ * _FNV_PRIME & _LBS_MASK) ^ b

    return hash_
