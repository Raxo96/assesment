# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version,
# all the versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether
# version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.

BAD_VER = None


def isBadVersion(n: int) -> bool:
    return n >= BAD_VER


def firstBadVersion(n: int) -> int:
    pass


if __name__ == "__main__":
    test_cases = [
        (1, 1),
        (5, 4),
        (10, 2),
        (30, 29),
        (100, 51),
        (94125, 424),
        (904909125, 1)
    ]
    for tc in test_cases:
        n, BAD_VER = tc
        answer = firstBadVersion(n)
        assert answer == BAD_VER, f'FAIL : {answer}, {BAD_VER}'
    print('PASS')
