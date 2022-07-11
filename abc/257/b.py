n,k,q = map(int,input().split())
A =  list(map(int,input().split()))
L =  list(map(int,input().split()))

for l in L:
  l = l - 1
  if A[l] == n:
    continue
  if A[l] + 1 in A:
    continue
  A[l] = A[l] + 1

print(*A)
    