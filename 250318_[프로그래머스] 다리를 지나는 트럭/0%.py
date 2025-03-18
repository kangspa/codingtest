from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    Q = deque(truck_weights)
    now_truck, now_count = 0, 0
    while Q:
        now_truck = Q.popleft()
        now_weight += now_truck
        now_count += now_truck
    return answer

if __name__=="__main__":
    bridge_length = [2, 100, 100]
    weight = [10, 100, 100]
    truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
    answer = [8, 101, 110]
    for b,w,t,a in zip(bridge_length, weight, truck_weights, answer):
        r = solution(b,w,t)
        print(f"{r==a} / 정답 : {a} / 출력 : {r}")