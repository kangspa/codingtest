from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    Remain = deque(truck_weights)
    Bridge = deque()
    Bridge.append([Remain.popleft(),1])
    while Remain or Bridge:
        # 우선 한칸씩 옮겨서 자리를 만든다.
        for truck in Bridge: truck[1] += 1
        answer += 1
        # 첫번째 트럭이 Bridge를 벗어났다면 제거해준다.
        if Bridge:
            if Bridge[0][1] > bridge_length: Bridge.popleft()
        # Bridge 위에 truck이 올라갈 수 있는지 확인 후, 가능하면 추가
        if sum(truck[0] for truck in Bridge)+Remain[0] <= weight:
            Bridge.append([Remain.popleft(), 1])
        # truck을 더 못 올리는 상황이라면, 첫번째 트럭을 최대한 한번에 옮기고 진행
        _, now = Bridge.popleft()
        n = (bridge_length+1)-now
        for truck in Bridge: truck[1] += n
        answer += n
    return answer

if __name__=="__main__":
    bridge_length = [2, 100, 100]
    weight = [10, 100, 100]
    truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
    answer = [8, 101, 110]
    for b,w,t,a in zip(bridge_length, weight, truck_weights, answer):
        r = solution(b,w,t)
        print(f"{r==a} / 정답 : {a} / 출력 : {r}")