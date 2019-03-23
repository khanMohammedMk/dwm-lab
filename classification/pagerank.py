import numpy as np
N=int(input("\nhow many no pages:"))
d=0.85
eps=1.0e-8
print("\please enter the adjacency matrix for the network")
print("\ntype 1 if there is a link from a page i to page j else type 0")
links = []
for i in range(0,N):
    L=[]
    for j in range(0,N):
        L.append(int(input('page '+str(i+1)+' to page '+str(j+1)+':')))
    links.append(L)  
outboundL=np.zeros(N,),dtype=int)
for i in range(0,N):
    for j in range(0,N):
        if(links[i][j]==1):
         outboundL[i]= outboundL[i]+1

 M=np.zeros((N,N))
 for i in range(0,N):
     for j in range(0,N):
         if links[j][i]==1:
             M[i][j] =1/outboundL[j]

  M=np.matrix(M)
  oneColMat=np.matrix(np.ones((N,1),dtype=int)) 

  R=np.matrix(np.full((N,1),1/N))

  while True;
    Rnext=d*np.dot(M,R)+((1-d)/N)*oneColMat
    diff=np.subtract(Rnext,R)
    if np.linalg.norm(diff) <eps:
        break
        R=Rnext                        