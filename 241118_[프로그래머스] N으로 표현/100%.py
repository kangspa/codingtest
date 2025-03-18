# 사칙연산 후 값 저장해주는 함수
def pmmd(visited, cnt, i1, i2):
    for n1 in visited[i1]:
        for n2 in visited[i2]:
            visited[cnt].add(n1+n2)
            visited[cnt].add(n1-n2)
            visited[cnt].add(n1*n2)
            if n2!=0:
                visited[cnt].add(n1//n2)

def solution(N, number):
    # 중복 연산 방지를 위해 set으로 설정
    visited = [set([0])] + [set([int(str(N)*i)]) for i in range(1,9)]
    # N과 number가 같다면, 1개만 사용하면 된다.
    if number==N: return 1
    # 사용하게 될 수는 1~8까지 / 1개 사용하는 경우는 앞서 확인했으니 2부터 체크
    for count in range(2, 9):
        for i in range(1, count):
            pmmd(visited, count, count-i, i)
            if number in visited[count]:
                return count
    return -1

if __name__ == '__main__':
    # testcase 1 : 4
    print(solution(5, 12))
    
    # testcase 2 : 3
    print(solution(2, 11))