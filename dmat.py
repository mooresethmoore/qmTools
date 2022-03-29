from sympy import *
import numpy as np



p00,p01,p10,p11=symbols("p00,p01,p10,p11")
symType=type(p00)
pA=Matrix([[p00,p01],[p10,p11]])

pauliX=Matrix([[0,1],[1,0]])
pauliY=Matrix([[0,-1j],[1j,0]])
pauliZ=Matrix([[1,0],[0,-1]])
paulis=[pauliX,pauliY,pauliZ]



def commute(A,B):
    return A*B - B*A


def creation(n,r=5):
    return Matrix([[np.sqrt(j+1) if i==j+1 else 0 for i in range(n)] for j in range(n)]).T

def ann(n):#annihilation
    return Matrix([[np.sqrt(j+1) if i==j+1 else 0 for i in range(n)] for j in range(n)])


def pMat(d): # d is dimension of matrix not system
    p=symbols("".join((f"p{str(row)}{str(col)}," for row in range(d) for col in range(d))))
    #not hermitian
    return Matrix([[p[col + row*d] for col in range(d)] for row in range(d)])


def tensorBasis(D,N): # 
    """
    returns d^n array (may end up with weird behavior for now if d>9
    so don't :)

    """
    dStr="".join((str(i)+"," for i in range(D)))
    
    return symbols("".join((f"{i}{chr(d)},")))

def dMat(psi): #let psi be a d^n array (d dimension n bits)
    pass



y,N=symbols("y,N")

H=Matrix([[-1,-y*(N-1)],[-y*(N-1),0]])

commute(paulis[0]*paulis[2],pauliY)
