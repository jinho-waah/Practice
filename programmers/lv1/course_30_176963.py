def solution(name, yearning, photo):
    answer = []
    name_dict = {name[i]: yearning[i] for i in range(len(name))}

    for people in photo:
        tmp = 0
        for person in people:
            if person in name_dict:
                tmp += name_dict[person]
        answer.append(tmp)

    return answer