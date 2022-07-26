N,M = map(int,input().split())
H =  list(map(int,input().split()))

todai = [[] for _ in range(N)]
for i in range(M):
    t1, t2 = map(int,input().split())
    todai[t1 - 1].append(t2 - 1)
    todai[t2 - 1].append(t1 - 1)
ans = 0
for i in range(N):
    if len(todai[i]) == 0:
        ans += 1
    else:
      flag = 0
      for j in todai[i]:
        if H[i] <= H[j]:
          flag = 1
        
      if flag == 0:
        ans += 1
print(ans)