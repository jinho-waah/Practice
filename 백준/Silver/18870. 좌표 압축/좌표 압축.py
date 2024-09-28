import sys
input = sys.stdin.readline

# 입력받기
N = int(input().strip())
coords = list(map(int, input().split()))

# 좌표 압축을 위한 정렬 후 순위 매기기
sorted_unique_coords = sorted(set(coords))  # 중복 제거 후 정렬

# 딕셔너리로 각 좌표의 압축된 값을 저장
coord_dict = {value: idx for idx, value in enumerate(sorted_unique_coords)}

# 원래 좌표 리스트를 압축된 값으로 변환하여 출력
compressed_coords = [coord_dict[x] for x in coords]
print(" ".join(map(str, compressed_coords)))
