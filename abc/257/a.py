# https://atcoder.jp/contests/arc131/tasks/arc131_b
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
s = []
n,x = map(int, input().split())
for i in range(26):
    for j in range(n):
        s.append(alphabet[i])

print(s[x-1])
