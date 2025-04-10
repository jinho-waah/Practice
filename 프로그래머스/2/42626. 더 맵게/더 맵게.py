import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트 전체를 힙으로 한 번에 변환
    answer = 0

    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            return answer

        if not scoville:  # 섞을 두 번째 음식이 없으면 실패
            return -1

        second = heapq.heappop(scoville)
        new = first + second * 2
        heapq.heappush(scoville, new)
        answer += 1

    return -1
