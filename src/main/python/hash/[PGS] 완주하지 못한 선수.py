import collections

# 문제 설명
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# 입출력 예
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    d = {}
    for i in participant:
        d[i] = d.get(i, 0) + 1

    for x in completion:
        d[i] -= 1
    return [k for k, v in d.items() if v > 0][0]


def solution2(participant, completion):
    d = {}
    temp = 0
    for i in participant:
        d[hash(i)] = i # hash-key(=key-value)
        temp += int(hash(i))
    for i in completion:
        temp -= hash(i)
    return d[temp]


def solution3(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


def solution4(participant, completion):
    return list(collections.Counter(participant) - collections.Counter(completion))[0]


# 실행
print(solution(participant, completion))