"""
def sn(a):
    b=[int(i) for i in str(a)]
    return a+sum(b)  

x=list(range(1,10001))

for i in range(1,10001):
    if sn(i) in x:
        x.remove(sn(i))

for i in x:
    print(i)
"""

a = [True]*10040
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                a[1001*i+101*j+11*k+2*l] = False
for i in range(10000):
    if a[i] == True:
        print(i)
