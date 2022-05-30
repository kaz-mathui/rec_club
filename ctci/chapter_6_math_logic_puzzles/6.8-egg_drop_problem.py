import cmath
import math

breaking_point = 99
count_drops = 0

# Worst case is 14 drops for this solution.


def quadratic_formula(a: int, b: int, c: int) -> int:
    """
    Finds the roots of a quadratic equation.
    """
    d = (b**2) - (4 * a * c)
    if d > 0:
        sq_delta = cmath.sqrt(d)
        x1 = (-b - sq_delta) / (2 * a)
        x2 = (-b + sq_delta) / (2 * a)
    return math.ceil(max(x1.real, x2.real))


def drop(floor: int) -> bool:
    """
    Determines if egg will break at this floor.
    Increases count of drops each time it is ran.
    """
    global count_drops
    global breaking_point
    count_drops += 1
    return floor >= breaking_point


def find_breaking_point(floors: int) -> int:
    """
    Finds breaking point by increasing egg1 at decreasing intervals and egg2
    at steady interval.
    """
    # To calculate interval, use:
    # x + (x - 1) + (x + 2) ... = floors
    # x(x + 1) / 2 = floors
    # or x**2 + x - floors * -2 = 0
    interval = quadratic_formula(1, 1, floors * -2)
    previous_floor = 0
    egg1 = interval

    # Drop egg1 at decreasing intervals.
    while not drop(egg1) and egg1 <= floors:
        interval -= 1
        previous_floor = egg1
        egg1 += interval

    # Drop egg2 at 1 unit increments.
    egg2 = previous_floor + 1
    while egg2 < egg1 and egg2 <= floors and not drop(egg2):
        egg2 += 1

    if egg2 > floors:
        return -1
    return egg2


if __name__ == "main":
    print("breaking point = " + str(find_breaking_point(100)))  # 99
    print("drops = " + str(count_drops))  # 14
