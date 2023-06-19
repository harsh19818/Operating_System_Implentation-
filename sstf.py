def sstf(l,head):
    n=len(l)
    seek=0
    for j in range(n):
        mdiff=9999
        for i in range(len(l)):
            diff=abs(head-l[i])
            if(diff<mdiff):
                mdiff=diff
                index=i
        head=l[index]
        seek+=mdiff
        print(l[index],' ',end=' ')
        l.pop(index)
sstf([176, 79, 34, 60, 92, 11, 41, 114],50)