# https://atcoder.jp/contests/arc131/tasks/arc131_b

H,W = map(int, input().split())
C = [[] for _ in range(H)]
for i in range(H):
    c = input()
    for j in range(W):
        C[i].append(c[j])

 
colors = list(['1','2','3','4','5'])
 
for i in range(H):
    for j in range(W):
        if C[i][j] == '.':
            used_color = []
            if j != 0:
                used_color.append(C[i][j-1])
            if j != W-1:
                used_color.append(C[i][j+1])
            if i != 0:
                used_color.append(C[i-1][j])
            if i != H-1:
                used_color.append(C[i+1][j])
            for x in colors:
                if x in used_color:
                    continue
                else:
                    C[i][j] = x
                    break
 
for i in range(H):
    c = ''.join(C[i])
    print(c)