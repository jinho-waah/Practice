# 돗자리 문제
def solution(mats, park):
    rows = len(park)
    cols = len(park[0])

    # 돗자리 크기를 내림차순으로 정렬
    mats.sort(reverse=True)

    # 주어진 크기의 돗자리가 공원에 깔릴 수 있는지 확인하는 함수
    def can_place(mat_size):
        for i in range(rows - mat_size + 1):
            for j in range(cols - mat_size + 1):
                # mat_size x mat_size 영역이 모두 "-1"인지 확인
                can_place_here = True
                for x in range(i, i + mat_size):
                    for y in range(j, j + mat_size):
                        if park[x][y] != "-1":
                            can_place_here = False
                            break
                    if not can_place_here:
                        break
                if can_place_here:
                    return True
        return False

    # 가장 큰 돗자리부터 확인
    for mat in mats:
        if can_place(mat):
            return mat

    return -1