def bestfit(block,m,process,n):
    allocation=[-1]*n
    for i in range(n):
        bestind=-1
        for j in range(m):
            if(block[j]>=process[i]):
                if bestind==-1:
                    bestind=j
                elif block[bestind]>block[j]:
                    bestind=j
        if bestind!=-1:
            allocation[i]=bestind
            block[bestind]-=process[i]
    print("process no.  process size  block no.")
    for i in range(n):
        print(i+1,"          ",process[i],end="          ")
        if(allocation[i]!=-1):
            print(allocation[i]+1)
        else:
            print('Not allocated')

block = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426]
m = len(block)
n = len(process)
 
bestfit(block, m, process, n)