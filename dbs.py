
import numpy as np
def solve(q1,q2,sumRows,sumCols):
    

    
    
    # print(Queryies[0][0],Queryies[1])
    # print(sumRows,sumCols)
    arr = np.concatenate((sumRows,sumCols))
    a = np.array(arr)


    #[3,7][3,9]                   ---------
    
   
    b=np.where(np.logical_and(a>=q1, a<=q2))
    print("Final",len(a[b]))




def main():
    R=int(input())
    C=int(input())
    mat=[[int(i) for i in input().split()] for i in range(R)]
    Q=int(input())
    _=int(input())
    Queryies=[]


    # print("Check",Q)

    sumRows=[sum(i) for i in mat]
    sumCols=[sum(i) for i in zip(*mat)]


    for i in range(Q):
        # print("khali",i)
        # solve(i,mat)
        Queryies.append([int(i) for i in input().split()])

        # print("xxx",Queryies[i][0],Queryies[i][1])
        solve(Queryies[i][0],Queryies[i][1],sumRows,sumCols)


    
    
    

main()
