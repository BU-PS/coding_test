# **(1/2) 제곱근
# % 1 하는 이유는 제곱근을 구했을때 소수점이 있으면 정수의 제곱근이 아님.
def solution(n):
    return -1 if n**0.5 % 1 else ((n**0.5)+1)**2