from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    Remain = deque(truck_weights)
    Bridge = deque()
    Bridge.append([Remain.popleft(),1])
    while Remain or Bridge:
        # 우선 한칸씩 옮겨서 자리를 만든다.
        answer += 1
        for truck in Bridge: truck[1] += 1
        # 첫번째 트럭이 Bridge를 벗어났다면 제거해준다.
        if Bridge and Bridge[0][1] > bridge_length: Bridge.popleft()
        # Bridge 위에 truck이 올라갈 수 있는지 확인 후, 가능하면 추가
        if Remain and sum(truck[0] for truck in Bridge)+Remain[0] <= weight:
            Bridge.append([Remain.popleft(), 1])
        # # truck을 더 못 올리는 상황이라면, 첫번째 트럭을 최대한 한번에 옮기고 진행
        # _, now = Bridge.popleft()
        # n = (bridge_length+1)-now
        # for truck in Bridge: truck[1] += n
        # answer += n
    return answer

if __name__=="__main__":
    bridge_length = [2, 100, 100]
    weight = [10, 100, 100]
    truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
    answer = [8, 101, 110]
    for b,w,t,a in zip(bridge_length, weight, truck_weights, answer):
        r = solution(b,w,t)
        print(f"{r==a} / 정답 : {a} / 출력 : {r}")

'''
def solution(bridge_length, weight, truck_weights):
    # bridge에 0을 채워서 마지막 트럭이 나올 때까지 걸리는 시간을 0의 갯수로 표시
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0 # sum(bridge)를 진행하는 것보다 별도의 변수를 만드는게 훨씬 효율적
    answer = 0
    # 원래 코드는 truck_weights.reverse()로 list 그대로 사용했으나, deque가 pop 작업이 훨씬 효율적
    truck_weights = deque(truck_weights)

    while truck_weights:
        answer += 1
        # 1턴의 시간이 지났음을 bridge 가장 좌측 값을 제거함으로써 표현
        total_weight -= bridge.popleft()
        # 다음에 들어오는 truck의 무게를 bridge가 못버틴다면 0을 bridge에 추가
        if total_weight + truck_weights[0] > weight:
            bridge.append(0)
        # 버틸 경우, 들어와야하는 truck을 bridge에 추가
        else:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
    # 남은 truck이 없다면, bridge 위에 있는 truck이 전부 빠져나오는데 걸리는 시간을 더한다.
    answer += bridge_length

    return answer
'''