from functools import partial
from typing import Callable


def create_path_finder(
        grid: dict[tuple[int, int], bool],
        rows: int,
        columns: int,
) -> Callable[..., list[tuple[int, int]]]:

    final_cell = (rows-1, columns-1)
    dead_end_cache: dict[tuple[int, int], None] = {}
    
    def find_path(r: int, c: int) -> list[tuple[int, int]]:
        if (r, c) == final_cell:
            return [(r, c)]
        
        path = []        
        
        is_walkable = grid.get((r, c), False)
        
        if is_walkable:
            next = (r+1, c)
            if next not in dead_end_cache:
                path = find_path(*next)
                if path[-1] != final_cell:
                    next = (r, c+1)
                    if next not in dead_end_cache:
                        path = find_path(*next)
                        if path[-1] != final_cell:
                            dead_end_cache[r, c] = None

        return [(r, c)] + path

    return partial(find_path, 0, 0)
    

if __name__ == "__main__":
    # 1 1 1 1 1
    # 1 1 1 1 0
    # 1 1 0 1 1
    # 1 1 1 0 1

    expected_path =[
            (0, 0),
            (1, 0), 
            (1, 1),
            (1, 2),
            (1, 3),
            (2, 3),
            (2, 4),
            (3, 4)
    ]

    rows = 4
    columns = 5
    grid = {(r, c): True for r in range(rows) for c in range(columns)}
    
    grid[1, 4] = False
    grid[2, 2] = False
    grid[3, 3] = False

    find_path = create_path_finder(grid, rows, columns)

    path = find_path()

    assert path == expected_path

    print(f"Path: {path}")
    


