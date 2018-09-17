import numpy as np
import matplotlib.pyplot as plt
import math

D=np.array([[0.697,0.460,1],[0.774,0.376,1],[0.634,0.264,1],[0.608,0.318,1],[0.556,0.215,1],[0.403,0.237,1],[0.481,0.149,1],[0.437,0.211,1],[0.666,0.091,0],[0.243,0.267,0],[0.245,0.057,0],[0.343,0.099,0],[0.639,0.161,0],[0.657,0.198,0],[0.360,0.370,0],[0.593,0.042,0],[0.719,0.103,0]])
x=[0.4,0.4]
y=[0,1]
x1=[0.6,0.6]
y1=[0,1]
x2=[0,1]
y2=[0.2,0.2]
as1=plt.subplot(121)
for i in range(len(D)):
    if(D[i][2]==1):
        plt.scatter(D[i][0],D[i][1],s=np.pi*(5)**2,c=1,alpha=0.5,marker=".")
    else:
        plt.scatter(D[i][0],D[i][1],s=np.pi*(5)**2,c=1,alpha=0.5,marker="+")

plt.plot(x,y,color="red")
plt.plot(x1,y1,color="blue")
plt.plot(x2,y2,color="green")
def h1(x1):
    if(x1>0.4):
        return 1
    else:
        return 0

def h2(x1):
    if(x1>0.6):
        return 1
    else:
        return 0

def h3(x2):
    if(x2>0.2):
        return 1
    else:
        return 0


m,n=D.shape[0],D.shape[1]

w=[1.0/17.0 for i in range(len(D))]

for j in range(1):
    e1,e2,e3=0,0,0
    for i in range(len(D)):
        if(h3(D[i][1])!=D[i][2]):
            e3+=w[i]

    a3=0.5*math.log(((1-e3)/e3),math.e)

    for i in range(len(D)):
        if(h3(D[i][1])!=D[i][2]):
            w[i]=w[i]/(2*e3)
        else:
            w[i]=w[i]/(2*(1-e3))

    for i in range(len(D)):
        if(h1(D[i][0])!=D[i][2]):
            e1+=w[i]

    a1=0.5*math.log(((1-e1)/e1),math.e)

    for i in range(len(D)):
        if(h1(D[i][0])!=D[i][2]):
            w[i]=w[i]/(2*e1)
        else:
            w[i]=w[i]/(2*(1-e1))

    for i in range(len(D)):
        if(h2(D[i][0])!=D[i][2]):
            e2+=w[i]
    a2=0.5*math.log(((1-e2)/e2),math.e)

    for i in range(len(D)):
        if(h2(D[i][0]!=D[i][2])):
            w[i]=w[i]/(2*e2)
        else:
            w[i]=w[i]/(2*(1-e2))

ax2=plt.subplot(122)
plt.plot([0,1],[0,1])
for i in range(len(D)):
    if((a1*h1(D[i][0])+a2*h2(D[i][0])+a3*h3(D[i][1])>0)):
        plt.scatter(D[i][0],D[i][1],s=np.pi*(5)**2,c=1,alpha=0.5,marker=".")
    else:
        plt.scatter(D[i][0],D[i][1],s=np.pi*(5)**2,c=1,alpha=0.5,marker="+")
plt.show()
