#이중 우선순위 큐
import heapq
import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    k = int(input())
    q_max, q_min = [], []
    visited = [False]*k

    for i in range(k):
        s, n = input().split()

        if s == 'I':
            heapq.heappush(q_max, (-int(n), i)) #최대 힙 (-를 붙여 제일 큰수를 최소로 만듬)
            heapq.heappush(q_min, (int(n), i)) #최소 힙
            visited[i] = True #정수 생성

        elif s == 'D':
            if n == '1':
                #만약 정수가 없다면(=False) 힙 제거
                while q_max and visited[q_max[0][1]] == False:
                    heapq.heappop(q_max)
                #최대힙 존재시 제거
                if q_max:
                    visited[q_max[0][1]] = False
                    heapq.heappop(q_max)

            else:
                #만약 정수가 없다면(=False) 힙 제거
                while q_min and visited[q_min[0][1]] == False:
                    heapq.heappop(q_min)
                #최소 힙 존재시 제거
                if q_min:
                    visited[q_min[0][1]] = False
                    heapq.heappop(q_min)

    if True not in visited: #정수 없으면 empty출력
        print("EMPTY")
    
    else: #정수가 없다면
        #존재하지 않는 정수(=False)제거
        while q_max and visited[q_max[0][1]] == False:
            heapq.heappop(q_max)
        while q_min and visited[q_min[0][1]] == False:
            heapq.heappop(q_min)
        #최대값(-붙여뒀음으로 다시 -로 +만들기), 최소값 출력
        print(-q_max[0][0], q_min[0][0])

        
