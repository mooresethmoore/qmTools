import sympy as sym

F,p=symbols("F,p")
bell=["phi","psi"]

bells=["\ket{\phi^{+}}","\ket{\psi^{-}}","\ket{\psi^{+}}","\ket{\phi^{-}}"]


input=[(i,j) for i in range(len(bells)) for j in range(len(bells))]

ps=["F"]+["p"]*3

out=[(0,0),(3,1),(0,2),(3,3),(1,2),(2,3),(1,0),(2,1),(2,2),(1,3),(2,0),(1,1),(3,0),(0,1),(3,2),(0,3)]



outTable=r"\begin{tabular}{||c |c |c| c||} "
outTable+=" \hline \n Prob & \ket{i}\ket{j} & After cNot & M_{2}(A)==M_{2}(B)? \\\ [0.5ex] \n \hline"


for i in range(len(input)):
    outTable+="\n"
    outTable+="\hline \n "
    outTable+=ps[input[i][0]]+ps[input[i][1]]+"&"
    outTable+="$"+bells[input[i][0]]+bells[input[i][1]] + "$ & "
    outTable+=$"+bells[out[i][0]]+bells[out[i][1]] + "$ & " 
    if 0==out[i][1] or  3==out[i][1]:
        outTable+=ps[input[i][0]]+ps[input[i][1]]
    else:
        outTable+="0"
    outTable+="\\\ \n \hline"

outTable+="\n\end{tabular}"


open("latexTable.txt","w").write(outTable)



f0=.6


fp=[f0]

steps=20
for i in range(steps):
    f=fp[-1]
    fp.append((f**2+(1-f)**2/9)/(f**2+(1-f)**2*5/9+2/3*f*(1-f)))

