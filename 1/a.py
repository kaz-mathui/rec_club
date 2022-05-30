
n = int(input())
p = list(map(int, input().split()))

sum = 0
for i in range(n - 2):
    if p[i] < p[i+1] < p[i+2]:
        sum += 1
    if p[i] > p[i+1] > p[i+2]:
        sum += 1
print(sum)