
n = int(input())
s = int(input())
W = list(map(int, input().split()))

for 

@njit('(i4[::1],)', cache=True)
def f(A):
    l.sort()
    ans = 0
    # print(l)
    for i in range(n):
        for j in range(i+1,n):
            print(l,bisect_left(l,l[i] + l[j]))
            for k in range(j+1,n):
                if l[i] + l[j] > l[k]:
                    ans += 1
            # ans += max(n - bisect_left(l,l[i] + l[j]) - 1,0)
    return ans

ans = f(l)
print(ans)