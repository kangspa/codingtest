from collections import deque
MOD = 1_000_000_007

def BFS(m, n, puddles):
    # 방문한 위치인지 확인 / 해당 위치까지 갈 수 있는 방법 / 0 인덱싱 넘버로 변경
    visited = [[False]*m for _ in range(n)]
    board = [[0]*m for _ in range(n)]
    for x, y in puddles:
        visited[y-1][x-1] = True
    # 이동 가능한 경로(방향, (x,y), 상하좌우)
    direction = ((0,-1),(0,1),(-1,0),(1,0))
    # Q에 현재 체크 중인 위치를 넣고 탐색 진행
    Q = deque()
    Q.append((0,0))
    board[0][0] = 1
    while Q:
        x, y = Q.popleft()
        if visited[y][x]: continue
        visited[y][x] = True
        # 이동 방향 전부 체크
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            # board 범위 안인지 확인
            if (0 <= nx < m) & (0 <= ny < n):
                # visited인 경우 pass
                if visited[ny][nx]: continue
                board[ny][nx] += board[y][x] % MOD
                Q.append((nx,ny))
    return board[n-1][m-1] % MOD

def solution(m, n, puddles):
    # dp 배열 초기화
    dp = [[0]*m for _ in range(n)]
    for x, y in puddles: dp[y-1][x-1] = -1
    # 시작점(집)은 1로 설정
    dp[0][0] = 1
    
    for y in range(n):
        for x in range(m):
            # puddles 위치는 못 지나가므로 pass
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            # 현위치로 올 수 있는 다른 경로의 수도 +
            if y > 0: dp[y][x] += dp[y-1][x]
            if x > 0: dp[y][x] += dp[y][x-1]
            dp[y][x] %= MOD
    return dp[n-1][m-1]

if __name__=="__main__":
    m, n = 4, 3
    puddles = [[2, 2]]
    answer = solution(m, n, puddles)
    print(f"{answer==4} / 정답 : 4 / 출력 : {answer}")