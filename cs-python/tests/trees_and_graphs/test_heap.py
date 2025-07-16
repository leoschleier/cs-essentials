from cs_essentials.trees_and_graphs.heap import MinHeap

class TestMinHeap:
    
    def test_min_heap(self) -> None:
        min_heap = MinHeap[int]()

        numbers = [3, 10, 4, 55, 0]

        for n in numbers:
            min_heap.insert(n)

        for n in sorted(numbers):
            assert min_heap.extract_min() == n
