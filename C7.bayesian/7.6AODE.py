import numpy as np
D=np.array([[1,1,1,1,1,1,0.697,0.460,1],[2,1,2,1,1,1,0.774,0.376,1],[2,1,1,1,1,1,0.634,0.264,1],[1,1,2,1,1,1,0.608,0.318,1],[3,1,1,1,1,1,0.556,0.215,1],[1,2,1,1,2,2,0.403,0.237,1],[2,2,1,2,2,2,0.481,0.149,1],[2,2,1,1,2,1,0.437,0.211,1],[2,2,2,2,2,1,0.666,0.091,0],[1,3,3,1,3,2,0.243,0.267,0],[3,3,3,3,3,1,0.245,0.057,0],[3,1,1,3,3,2,0.343,0.099,0],[1,2,1,2,1,1,0.639,0.161,0],[3,2,2,2,1,1,0.657,0.198,0],[2,2,1,1,2,2,0.360,0.370,0],[3,1,1,3,3,1,0.593,0.042,0],[1,1,2,2,2,1,0.719,0.103,0]])
test=[1,1,1,1,1,1,0.697,0.460]
m,n=D.shape[0],D.shape[1]
p1=[0 for i in range(6)]
q1=[0 for i in range(6)]
t=[3,3,3,3,3,2]
pp=[0 for i in range(6)]
qq=[0 for i in range(6)]
for i in range(8):
    for j in range(6):
        if(D[i][j]==test[j]):
            p1[j]+=1
            pp[j]+=1
for i in range(8,17):
    for j in range(6):
        if(D[i][j]==test[j]):
            q1[j]+=1
            qq[j]+=1

for i in range(6):
    p1[i]=(p1[i]+1)/(17+2*t[i])
for i in range(6):
    q1[i]=(q1[i]+1)/(17+2*t[i])
def pro(d,t):
    mean=np.mean(d);
    var=np.var(d);
    k=np.exp(-(t-mean)**2/(2*var))/(np.sqrt(2*np.pi*var))
    return k
result=[1 for i in range(6)]
result2=[1 for i in range(6)]
for i in range(6):
    p2=[0 for i in range(6)]
    q2=[0 for i in range(6)]
    for j in range(8):
        for l in range(6):
            if((D[j][l]==test[l])and(D[j][i]==test[i])):
                p2[l]+=1
    for j in range(8,17):
        for l in range(6):
            if((D[j][l]==test[l])and(D[j][i]==test[i])):
                q2[l]+=1
    for f in range(6):
        p2[f]=(p2[f]+1)/(pp[f]+t[f])
        q2[f]=(q2[f]+1)/(qq[f]+t[f])
    s,s2=1,1
    for g in range(6):
        s*=p2[g]
        s2*=q2[g]
    result[i]=s*pro(D[:8,6],test[-2])*pro(D[:8,7],test[-1])*p1[i]
    result2[i]=s2*pro(D[8:,6],test[-2])*pro(D[8:,-7],test[-1])*q1[i]
all1=float(0.0)
all2=float(0.0)
for i in range(6):
    all1=all1+result[i]
    all2=all2+result2[i]
print(all1)
print(all2)




