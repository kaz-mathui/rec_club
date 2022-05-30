from typing import List


class Bottle:
    def __init__(self, id: int):
        """
        Bottle constructor.
        """
        self.poisoned = False
        self.__id = id

    @property
    def id(self) -> int:
        """
        Id getter.
        """
        return self.__id

    @id.setter
    def id(self, id: int):
        """
        Id setter.
        """
        self.__id = id

    def set_as_poisoned(self):
        """
        Set a bottle as poisoned.
        """
        self.poisoned = True

    def is_poisoned(self) -> bool:
        """
        Determines if a bottle is poisoned or not.
        """
        return self.poisoned


class TestStrip:
    def __init__(self, id: int):
        """
        TestStrip constructor.
        """
        self.DAYS_FOR_RESULT = 7
        self.__drops_by_day = []
        self.__id = id

    @property
    def id(self) -> int:
        """
        Id getter.
        """
        return self.__id

    @id.setter
    def id(self):
        """
        Id setter.
        """
        self.__id = id

    def size_drops_for_day(self, day: int):
        """
        Resize list of days/drops to be large enough.
        """
        while len(self.__drops_by_day) <= day:
            self.__drops_by_day.append([])

    def add_drop_on_day(self, day: int, bottle: Bottle):
        """
        Add drop from bottle on specific day.
        """
        self.size_drops_for_day(day)
        drops = self.__drops_by_day[day]
        drops.append(bottle)

    def has_poison(self, bottles: List[Bottle]) -> bool:
        """
        Checks if any of the bottles in the set are poisoned.
        """
        for b in bottles:
            if b.is_poisoned():
                return True
        return False

    def is_positive_on_day(self, day: int) -> bool:
        """
        Checks for poisoned bottles since before DAYS_FOR_RESULT.
        """
        test_day = day - self.DAYS_FOR_RESULT
        if test_day < 0 or test_day > len(self.__drops_by_day):
            return False
        for i in range(test_day + 1):
            bottles = self.__drops_by_day[i]
            if self.has_poison(bottles):
                return True
        return False


def find_poisoned_bottle(bottles: List[Bottle], strips: List[TestStrip]) -> int:
    """
    Finds the poisoned bottle in the minimum amount of days.
    Will work as long as 2**T >= B, where T is the number of test strips and
    B is the number of bottles.
    """
    run_tests(bottles, strips)
    positive = get_positive_on_day(strips, 7)
    return set_bits(positive)


def run_tests(bottles: List[Bottle], test_strips: List[TestStrip]):
    """
    Add bottle contents to test strips.
    """
    for b in bottles:
        bit_index = 0
        while (b.id > 0):
            if ((b.id & 1) == 1):
                test_strips[bit_index].add_drop_on_day(0, b)
            bit_index += 1
            b.id >>= 1


def get_positive_on_day(test_strips: List[TestStrip], day: int) -> List[int]:
    """
    Get test strips that are positive on a particular day.
    """
    positive = []
    for t in test_strips:
        if t.is_positive_on_day(day):
            positive.append(t.id)
    return positive


def set_bits(positive: List[int]) -> int:
    """
    Create number by setting bits with indices specified in positive.
    """
    id = 0
    for bit_index in positive:
        id |= 1 << bit_index
    return id


if __name__ == "main":
    bottles = []
    for i in range(0, 1000):
        b = Bottle(i)
        # set poisoned bottle
        if i == 995:
            b.set_as_poisoned()
        bottles.append(b)
    test_strips = []
    for i in range(0, 10):
        t = TestStrip(i)
        test_strips.append(t)

    print(find_poisoned_bottle(bottles, test_strips))  # 995
