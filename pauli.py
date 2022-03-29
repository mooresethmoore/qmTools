from sympy import *
import numpy as np

def con

pauliX=np.matrix([[0,1],[1,0]])
pauliY=np.matrix([[0,1j],[1j,0]])
pauliZ=np.matrix([[1,0],[0,-1]])
paulis=[pauliX,pauliY,pauliZ]





p00,p01,p10,p11=symbols("p00,p01,p10,p11")
pA=np.array([[p00,p01],[p10,p11]])



epsX=pauliX.dot(pA).dot(pauliX) # flips all elements: 
epsY=pauliY.dot(pA).dot(pauliY) # flips all elements,(phase) flips sign of off diag 
epsZ=pauliZ.dot(pA).dot(pauliZ) # keeps all elements, (phase) flips sign of off diag






pauliX=Matrix([[0,1],[1,0]])
pauliY=Matrix([[0,-1j],[1j,0]])
pauliZ=Matrix([[1,0],[0,-1]])
paulis=[pauliX,pauliY,pauliZ]
pA=Matrix([[p00,p01],[p10,p11]])





c=symbols("cx,cy,cz")

pPrime=zeros(2,2)

primes=[]

for i in range(len(paulis)):
    primes.append(paulis[i]*pA*paulis[i])
    pPrime=(paulis[i]*c[i])*pA*paulis[i]+pPrime



m01=Matrix([[0,sqrt(c[0])],[0,0]])
pProj01=m01*pA*m01.T


m10=m01.T
pProj10=m10*pA*m10.T

m00=Matrix([[sqrt(c[0]),0],[0,0]])
pProj00=m00*pA*m00

m11=Matrix([[0,0],[0,sqrt(c[0])]])
pProj11=m11*pA*m11


mtest=Matrix([[1,0],[0,sqrt(c[0])]])
print(mtest*pA*mtest)

proj=symbols("c00,c01,c10,c11")

superOps={}
one=ones(2,2)
for i in range(len(proj)):
    mProj=zeros(2,2)
    mProj[int(str(proj[i])[1]),int(str(proj[i])[2])]=1
    superOps.update({str(proj[i]):mProj*pA*mProj.T*proj[i]})



bVec=symbols("px,py,pz")
pB=Matrix([[1+bVec[2],bVec[0]-1j*bVec[1]],[bVec[0]+1j*bVec[1],1-bVec[2]]])

pPrime=zeros(2,2)

primes=[]

for i in range(len(paulis)):
    primes.append(paulis[i]*pB*paulis[i])
    pPrime=(paulis[i]*c[i])*pB*paulis[i]+pPrime



pAB=zeros(4,4)
for i in range(4):
    for j in range(4):
        pAB[i,j]=symbols("p"+str(i)+str(j))
