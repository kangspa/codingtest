from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    Remain = deque(truck_weights)
    Bridge = deque()
    while Remain:
        tmp = None
        # Bridge에 트럭을 계속해서 추가해나가는 부분
        while True:
            # Bridge[0]의 합이 weight을 넘기면 마지막에 넣은 트럭은 우선 제거해두고 진행
            if sum(b[0] for b in Bridge) > weight:
                tmp = Bridge.pop()
                break
            # 하중을 넘기지 않았다면, 우선 Bridge 안의 트럭을 1대씩 앞으로 이동
            for truck in Bridge: truck[1] += 1
            # 첫번째 truck의 위치가 bridge_length를 넘기면 Bridge에서 제거
            if Bridge:
                if Bridge[0][1] > bridge_length: Bridge.popleft()
            # Bridge에 다음 truck을 추가해준다.
            if Remain: Bridge.append([Remain.popleft(), 1])
            answer += 1
        # Bridge에 더이상 truck이 올라가지 못하는 경우, 첫번째 트럭이 나갈 때까지 한번에 연산
        _, now = Bridge.popleft()
        n = (bridge_length+1)-now
        for truck in Bridge: truck[1] += n
        answer += n
        # tmp에 저장해뒀던, 넣었다 뺀 트럭 정보를 다시 입력해준다.
        Bridge.append(tmp)
    return answer

if __name__=="__main__":
    bridge_length = [2, 100, 100]
    weight = [10, 100, 100]
    truck_weights = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]
    answer = [8, 101, 110]
    for b,w,t,a in zip(bridge_length, weight, truck_weights, answer):
        r = solution(b,w,t)
        print(f"{r==a} / 정답 : {a} / 출력 : {r}")