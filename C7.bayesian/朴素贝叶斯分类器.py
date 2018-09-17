import numpy as np
import math
D=np.array([[1,1,1,1,1,1,0.697,0.460,1],[2,1,2,1,1,1,0.774,0.376,1],[2,1,1,1,1,1,0.634,0.264,1],[1,1,2,1,1,1,0.608,0.318,1],[3,1,1,1,1,1,0.556,0.215,1],[1,2,1,1,2,2,0.403,0.237,1],[2,2,1,2,2,2,0.481,0.149,1],[2,2,1,1,2,1,0.437,0.211,1],[2,2,2,2,2,1,0.666,0.091,0],[1,3,3,1,3,2,0.243,0.267,0],[3,3,3,3,3,1,0.245,0.057,0],[3,1,1,3,3,2,0.343,0.099,0],[1,2,1,2,1,1,0.639,0.161,0],[3,2,2,2,1,1,0.657,0.198,0],[2,2,1,1,2,2,0.360,0.370,0],[3,1,1,3,3,1,0.593,0.042,0],[1,1,2,2,2,1,0.719,0.103,0]])

c=[0,0]
for i in range(len(D)):
    if(D[i,-1]==1):
        c[1]+=1
    else:
        c[0]+=0
p1=[0,0,0,0,0,0]
for i in range(8):
    for j in range(6):
        if(D[i][j]==1):
            p1[j]+=1
p0=[0,0,0,0,0,0]
for i in range(8,17):
    for j in range(6):
        if(D[i][j]==1):
            p0[j]+=1
p=[0,0,0,0,0,0]
for i in range(len(D)):
    for j in range(6):
        if(D[i][j]==1):
            p[j]+=1
for i in range(len(D)):
    for j in range(6):
        p1[j]/=8
        p0[j]/=8
        p[j]/=17

midu=[0 for l in range(17)]
hant=[0 for l in range(17)]
def pro(d,t):
    m=np.mean(d);
    v=np.var(d);
    pp=np.exp(-(t-m)**2/(2*v))/(np.sqrt(2*np.pi*v))
    return pp
test=[1,1,1,1,1,1,0.697,0.460]

P1,P0=8/17,9/17
for i in range(6):
    P1*=p1[i]
    P0*=p0[i]

P1*=pro(D[:8,6],test[-2])*pro(D[:8,7],test[-1])
P0*=pro(D[8:,6],test[-2])*pro(D[8:,7],test[-1])
for i in range(6):
    P1/=p[i]
    P0/=p[i]

print(P1,P0)
