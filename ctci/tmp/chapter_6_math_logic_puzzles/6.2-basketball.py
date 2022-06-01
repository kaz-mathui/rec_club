"""
Probability of winning game 1: p
Probability of winning game 2:
Winning = 2 shots or 3 shots
P(winning) = s(2, 3) + s(3, 3)
3 shots
s(3, 3) = p**3
2 shots
P(making 1 and 2 and missing 1) +
P(making 1 and 3 and missing 2) +
P(missing 1 and making 2 and 3)
= p * p (1 - p) * (1 - p) * p + (1 - p) * p * p
= 3 (1 - p) p**2
What game should you play:
You should play Game 1 if P(Game 1) > P(Game 2)
p > 3p**2 - 2p**3
1 > 3p - 2p**2
2p**2 - 3p + 1 > 0
(2p - 1)(p - 1) > 0
Both terms must be positive or both must be negative. But we know p < 1 so
p - 1 < 0.
This means both terms must be negative.
2p - 1 < 0
2p < 1
p < .5
So we should play Game 1 if 0 < p < .5 and Game 2 if .5 < p < 1
If p = 0, 0.5, or 1, then it doesn't matter
"""
