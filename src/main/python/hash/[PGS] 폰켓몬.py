# 문제 설명
# N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때,
# N/2마리의 폰켓몬을 선택하는 방법 중, 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아,
# 그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
nums = [3,1,2,3]

def solution(nums):
    return min(len(set(nums)), len(nums)/2)


# 실행
print(solution(nums))