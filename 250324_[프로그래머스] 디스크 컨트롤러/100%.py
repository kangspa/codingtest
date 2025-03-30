from collections import deque
import heapq

def solution(jobs):
    answer = 0
    # 요청 시간 기준으로 정렬
    jobs.sort()
    Q = deque(jobs)
    heap = []
    time, count = 0, 0
    
    while count < len(jobs):
        # 현재 시간(time)까지 실행 가능한 작업들을 힙에 추가
        while Q and Q[0][0] <= time:
            s, l = Q.popleft()
            heapq.heappush(heap, (l, s))
        # 추가된 작업 중 우선 진행 가능한 작업 추출
        if heap:
            l, s = heapq.heappop(heap)
            time += l
            answer += (time - s)
            count += 1
        # 실행할 작업이 없으면 시간 이동
        else:
            time = Q[0][0]

    return answer // len(jobs)


if __name__=="__main__":
    jobs = [[0, 3], [1, 9], [3, 5]]
    answer = solution(jobs)
    print(f"{answer==8} / 정답 : 8 / 출력 : {answer}")