import timeit


def memoize(func):
    """
    Decorator to memoize recursive functions.
    """
    memory = {}

    def helper(n: int) -> int:
        if n not in memory:
            memory[n] = func(n)
        return memory[n]
    return helper

# naive solution


def count_ways(n: int) -> int:
    """
    Count the possible ways a child can run up the stairs if they can take
    either 1, 2, or 3 steps at a time.
    O(3**n) solution.
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


@memoize
def count_ways_memo(n: int) -> int:
    """
    Count the possible ways a child can run up the stairs if they can take
    either 1, 2, or 3 steps at a time.
    O(n) solution
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return (count_ways_memo(n - 1) +
            count_ways_memo(n - 2) +
            count_ways_memo(n - 3))


ex = 25
res1 = timeit.timeit("count_ways(ex)", globals=globals(), number=1)
res2 = timeit.timeit("count_ways_memo(ex)", globals=globals(), number=1)
print(res1)  # ~5.606339116000072
print(res2)  # ~4.505800006882055e-05
print(res1 / res2)  # ~124424 times slower
