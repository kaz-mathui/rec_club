from collections import deque
import itertools

n = int(input())
A = deque(map(int, input().split()))
q = int(input())
Q = []
for i in range(q):
    l, r, x = map(int, input().split())
    Q.append((l-1, r-1, x))
    
for i in range(q):
    l, r, x = Q[i]
    # print(l, r, x)
    A_after = deque(itertools.islice(A, l, r+1))
    # print(A_after)
    
    print(A_after.count(x))