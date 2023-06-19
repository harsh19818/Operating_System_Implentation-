def firstfit(block,m,pr,n):
    allocation=[-1]*n
    for i in range(n):
        for j in range(m):
            if block[j]>=pr[i]:
                allocation[i]=j
                block[j]-=pr[i]
                break
    print("process no.  process size  block no.")
    for i in range(n):
        print(i+1,"        ",process[i],end="        ")
        if(allocation[i]!=-1):
            print(allocation[i]+1)
        else:
            print('Not allocated')

block = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426]
m = len(block)
n = len(process)
 
firstfit(block, m, process, n)