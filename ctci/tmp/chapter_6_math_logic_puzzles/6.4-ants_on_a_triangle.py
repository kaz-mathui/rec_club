"""
P(clockwise) = (1/2)**3
P(counter clockwise) = (1/2)**3
P(same direction) = (1/2)**3 + (1/2)**3 = 1/4
The probability of collision is therefore the probability of the ants not
moving in the same direction.
P(collision) = 1 - P(samedirection) = 1 - 1/4 = 3/4
To generalize this to an n-vertex polygon, there are still only two ways in
which the ants can move to avoid collsion, but there are 2**n ways they can
move in total.
P(clockwise) = (1/2)**n
P(counter clockwise) = (1/2)**n
P(same direction) = (1/2)**n + (1/2)**n = (1/2)**(n - 1)
P(collision) = 1 - P(samedirection) = 1 - (1/2)**(n - 1)
"""
