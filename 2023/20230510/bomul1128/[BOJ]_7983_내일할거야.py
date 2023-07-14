import sys
i=sys.stdin.readline
n=int(i())
w=[list(map(int,i().split()))[::-1]for _ in' '*n]
w.sort();l=w[-1][0]
for y,x in w[::-1]:
 l=min(l,y)-x
print(l)