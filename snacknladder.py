t = int(input())
for _ in range(t):
    dq=[]
    ladder={}
    snake={}
    visited={}
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(0,2*n,2):
        if arr[i] < arr[i+1]:
            ladder[arr[i]] = arr[i+1]
        else:
            snake[arr[i]] = arr[i+1]
    dq.append((1,0))
    while dq:
        pos,throws = dq.pop(0)
        if pos == 30:
            break
        if pos not in visited:
            for i in range(1,7):
                new_pos = pos + i
                if new_pos <= 30 and new_pos not in visited:
                    if new_pos in ladder:
                        dq.append((ladder[new_pos],throws+1))
                    elif new_pos in snake:
                        dq.append((snake[new_pos],throws+1))
                    else:
                        dq.append((new_pos,throws+1))

                        
    print (throws)
