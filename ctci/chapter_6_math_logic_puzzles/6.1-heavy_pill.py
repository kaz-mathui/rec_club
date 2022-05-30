"""
1. Take one pill from Bottle #1, two pills from Bottle #2, three pills from
Bottle #3, and so on.
2. Weight this mix of pills.
3. If all pills were one gram each, the scale would read 210 grams
(1 + 2 + ... + 20 = 20 * 21 / 2 = 210)
4. Any "overage" must come from the extra 0.1 game pills.
5. This formula will tell you the bottle number:
    weight - 210 grams
    ------------------
        0.1 grams
6. So, if the set of pills weighted 211.3 grams, then Bottle #13 would have
the heavy pills.
"""
