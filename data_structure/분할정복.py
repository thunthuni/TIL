arr = [234, 54, 35, 6, 2, 364, 346, 100]

# 1. 정렬된 상태의 데이터
arr.sort()

# 2. 이진 검색 - 반복문 버전
def binarySearch(target):
    # 제일 왼쪽, 오른쪽 인덱스 구하기
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) //2
        