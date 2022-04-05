#나무 자르기

n, m = map(int,input().split())

tree = list(map(int,input().split()))
start = 1
last = max(tree)
while True:
    
    mid = (start+last) //2
    count = 0
    for i in tree:
        if i > mid:
            count =count + (i - mid)

    if count == m:
        print(mid)
        break

    elif count > m:
        start = mid+1
    
    elif count < m:
        last = mid-1
