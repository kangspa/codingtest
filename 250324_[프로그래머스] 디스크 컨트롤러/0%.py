import heapq

def solution(jobs):
    answer = 0
    heap = []
    for i, job in enumerate(jobs):
        heapq.heappush(heap, (job[1], job[0], i))

    disk_time = -1
    while heap:
        spend_time, start_time, _ = heapq.heappop(heap)
        if (disk_time == -1) or (disk_time < start_time):
            disk_time=start_time
        disk_time += spend_time
        answer += (disk_time-start_time)
    answer //= len(jobs)
    return answer