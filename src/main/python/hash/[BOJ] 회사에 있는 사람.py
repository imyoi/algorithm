import sys
# 문제 설명
# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다.
# 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
# "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.
# 회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다.
# 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

# 입출력 예
# 4
# Baha enter
# Askar enter
# Baha leave
# Artem enter

def solution():
    # n줄 입력 시
    n = int(sys.stdin.readline())
    d = {}

    for i in range(n):
        name, status = sys.stdin.readline().split()
        if status == 'enter': d[name] = status
        else: del d[name]

    for i in sorted(d, reverse=True):
        print(i)


# 실행
solution()