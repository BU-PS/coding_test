# 문제 설명
# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
#
# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.
#
# 10진법	124 나라	10진법	124 나라
# 1	    1	    6	    14
# 2	    2	    7	    21
# 3	    4	    8	    22
# 4	    11	    9	    24
# 5	    12	    10	    41
# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
#
# 제한사항
# n은 500,000,000이하의 자연수 입니다.
import unittest


def solution(n):
    answer = ""
    one_two_four_map = {
        0: "1",
        1: "2",
        2: "4"
    }

    n_count = 0
    number = 0
    # 3 ** 20 > 500,000,000
    i = 20

    if n < 4:
        return one_two_four_map[n - 1]

    for i in range(1, i + 1):
        number += 3 ** i

        if n < number:
            n_count = i
            break

    for j in range(n_count):
        answer += one_two_four_map[(n - 1) % 3]
        n = (n - 1) // 3

    return answer[::-1]



class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._n = 3
        self._answer = 41

    def test_solution(self):
        result = solution(n=self._n)


if __name__ == '__main__':
    unittest.main()
