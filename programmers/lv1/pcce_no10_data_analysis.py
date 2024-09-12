#데이터 분석
def solution(data, ext, val_ext, sort_by):
    answer = []
    sort_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    delete_index = sort_dict[ext]

    for data_one in data:
        if data_one[delete_index] < val_ext:
            answer.append(data_one)

    answer.sort(key=lambda x: x[sort_dict[sort_by]])
    return answer