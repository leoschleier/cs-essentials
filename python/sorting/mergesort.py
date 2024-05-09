
def sort(elements: list[int]) -> list[int]:
    print(f"Sort: {elements}")
    if len(elements) > 1:
        left_half, right_half = split(elements)
        
        left_half_sorted = sort(left_half)
        right_half_sorted = sort(right_half)
 
        merged = merge(left_half_sorted, right_half_sorted)
        print(f"Merged: {merged}")

        return merged
    else:
        return elements
    

def split(elements: list[int]) -> tuple[list[int], list[int]]:
    mid = len(elements) // 2
    left_half = elements[:mid]
    right_half = elements[mid:]
    return left_half, right_half

def merge(left: list[int], right: list[int]):
    if len(left) == 0 or len(right) == 0:
        return left + right

    merged = [] 
    idx = 0
    for l in left:
        i = idx
        for r in right[i:]:
            if r <= l:
                merged.append(r)
            else:
                break
            idx += 1
        merged.append(l)
    
    merged += right[idx:]

    return merged

if __name__ == "__main__":
    sorted = sort([13, 11, 12, 5, 6, 7])
    print(f"Result: {sorted}")