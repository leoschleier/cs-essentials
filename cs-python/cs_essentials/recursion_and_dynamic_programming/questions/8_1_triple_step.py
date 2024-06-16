import time


_cache: dict[int, int] = {}


def compute_paths(n: int) ->int:
    if n < 0:
        return 0
    elif n == 0:
        return 1

    return compute_paths(n-1) + compute_paths(n-2) + compute_paths(n-3)


def compute_paths_memoize(n: int) ->int:
    if n < 0:
        return 0
    elif n == 0:
        return 1

    if (n_paths := _cache.get(n)) is None:
        n_paths = (
            compute_paths_memoize(n-1)
            + compute_paths_memoize(n-2)
            + compute_paths_memoize(n-3)
        )
        _cache[n] = n_paths


    return n_paths


if __name__ == "__main__":
    for n in range(0, 31, 5):
        start = time.time()
        paths = compute_paths(n)
        runtime = time.time() - start

        start = time.time()
        paths_m = compute_paths_memoize(n)
        runtime_m = time.time() - start
        _cache = {}

        assert paths == paths_m

        print(
            f"Paths for {n} steps: {paths} | Runtime: {runtime}s, "
            f"with memoization: {runtime_m}s"
        )

