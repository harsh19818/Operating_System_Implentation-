def bestfit(block,m,process,n):
    allocation=[-1]*n
    for i in range(n):
        best=-1
        for j in range(m):
            if block[j]>=process[i]:
                if best==-1:
                    best=j
                elif block[best]>block[j]:
                    best=j
        if best!=-1:
            allocation[i]=best
            block[best]-=process[i]
    print('process no. process size block no.')
    for i in range(n):
        print(i+1,'            ',process[i],end='            ')
        if allocation[i]!=-1:
            print(allocation[i]+1)
        else:
            print('NAN')
block = [100, 500, 200, 300, 600]
process = [212, 417, 112, 426]
m = len(block)
n = len(process)
 
bestfit(block, m, process, n)