class Tower:
    def __init__(self, i: int):
        """
        Tower constructor.
        """
        self.disks = []
        self.index = i

    def add(self, d: int):
        """
        Adds a value to the top of the tower.
        """
        if len(self.disks) and self.disks[-1] <= d:
            print(self)
            print(self.disks[-1])
            raise Exception("Error placing " + str(d))
        else:
            self.disks.append(d)

    def move_top_to(self, tower):
        """
        Moves a value from the top of a tower to another tower.
        """
        top = self.disks.pop()
        tower.add(top)

    def move_disks(self, n: int, dest, buff):
        """
        Moves all values from one tower to another using a buffer.
        """
        if n > 0:
            self.move_disks(n - 1, buff, dest)
            self.move_top_to(dest)
            print(f"moving {n} from {self} to {dest}")
            buff.move_disks(n - 1, dest, self)

    def __str__(self) -> str:
        """
        String representation.
        """
        return "Tower " + str(self.index)


num_of_disks = 3
towers = []
for i in range(3):
    towers.append(Tower(i))
for i in range(num_of_disks - 1, -1, -1):
    towers[0].add(i)

print(towers[0].disks)
# [2, 1, 0]

towers[0].move_disks(num_of_disks, towers[2], towers[1])
"""
moving 1 from Tower 0 to Tower 2
moving 2 from Tower 0 to Tower 1
moving 1 from Tower 2 to Tower 1
moving 3 from Tower 0 to Tower 2
moving 1 from Tower 1 to Tower 0
moving 2 from Tower 1 to Tower 2
moving 1 from Tower 0 to Tower 2
"""
print(towers[2].disks)  # [2, 1, 0]
