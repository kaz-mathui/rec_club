"""
Case c = 1: Exactly one person
Person will realize that nobody else has blue eyes. Will leave first night.
Case c = 2: Exactly 2 people
The two blue eyed people see each other, but are unsure whether c is 1 or 2. 
Since nobody left the first night, each person can deduce c > 1. Since nobody
else has blue eyes, they will both leave second night.
Case c > 2: The general case
The same pattern extends up to any value of c. Therefore, if c men have blue
eyes, it will take c nights.
"""
