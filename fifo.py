size=8;
def fifo(arr,head):
    seek=0
    dist=0
    cur=0
    for i in range(size):
        cur=arr[i]
        dist=abs(head-cur)
        seek+=dist
        head=cur
    print(seek)
    print(arr)
arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ];
head = 50;
fifo(arr, head);