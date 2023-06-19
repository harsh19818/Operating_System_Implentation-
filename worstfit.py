def worstfit(block,m,process,n):
    allocation=[-1]*n
    for i in range(n):
        worstind=-1
        for j in range(m):
            if block[j]>=process[i]:
                if worstind==-1:
                    worstind=j
                elif block[worstind]<block[j]:
                    worstind=j
        if worstind!=-1:
            allocation[i]=worstind
            block[worstind]-=process[i]
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
 
worstfit(block, m, process, n)