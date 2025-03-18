def solution(nums):
    n = len(nums)//2
    k = len(set(nums))
    # 두 값 중 더 작은 값이 가질 수 있는 최대 포켓몬 종류
    return n if n<k else k

if __name__ == '__main__':
    testcase = [3,1,2,3]
    print(solution(testcase)) #2
    
    testcase = [3,3,3,2,2,4]
    print(solution(testcase)) #3
    
    testcase = [3,3,3,2,2,2]
    print(solution(testcase)) #2