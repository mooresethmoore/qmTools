import numpy as np 
from math import sqrt



def outer(x,y): return np.outer(x,y.conjugate())


def qWalkCoin(x0,steps,storeCount=2):
    states=[]
    cur=x0.copy()
    rule={"up":1,"down":-1}
    for i in range(steps):
        if i%storeCount==0:
            states.append(cur.copy())
        adder=[]
        for k in cur.keys():
            vNew=k[1]+rule[k[0]]
            #print(f"k {k} \n vNew: {vNew}\n\n")
            nex={("up",vNew):1/np.sqrt(2)*cur[k], ("down",vNew):rule[k[0]]/np.sqrt(2)*cur[k]} ##future thread
            adder.append(nex)
        cur=dict()
        for j in adder:
            for newState in j.keys():
                if newState in cur:
                    supPos=cur[newState]+j[newState]
                    if np.isclose(np.absolute(supPos),0):
                        cur.pop(newState)
                    else:
                        cur[newState]=supPos
                else:
                    cur[newState]=j[newState].copy()
            ##normalize
        c=np.sum([np.absolute(v)**2 for v in cur.values()])
        cur={k:v/np.sqrt(c) for k,v in cur.items()}
    return states


x0={("up",0):1/np.sqrt(2),("down",0):1/np.sqrt(2)*1j}

p2=qWalkCoin(x0,100)

