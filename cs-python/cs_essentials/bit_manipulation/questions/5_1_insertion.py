
_BIT_MASK_32 = 2**32 - 1

def insert(n: int, m: int, i: int, j: int) -> str:
    # NNNNNNNNNNNNN & 1111000001111 -> NNNN00000NNNN 
    # NNNN00000NNNN | 0000MMMMM0000 -> NNNNMMMMMNNNN
    mask1 = 0b0
    for s in range(i, j+1):
        mask1 = mask1 | (0b1 << s)
    mask0 = not_32(mask1) 
    
    n_masked = n & mask0
    m_masked = ((_BIT_MASK_32 ^ m ^ _BIT_MASK_32) << i)

    return bin(n_masked | m_masked)


def not_32(b: int, /) -> int:
    """Bitwise NOT that works as if we were using unsigned integers."""
    return ~b & _BIT_MASK_32



if __name__ == "__main__":
    n = int("10000000000", 2)
    m = int("10011", 2)
    i = 2
    j = 6
    
    result = insert(n, m, i, j,)
    print(f"Result: {result}")
    
    
    n = int("11111111111", 2)
    m = int("10011", 2)
    i = 2
    j = 6

    result = insert(n, m, i, j,)
    print(f"Result: {result}")

