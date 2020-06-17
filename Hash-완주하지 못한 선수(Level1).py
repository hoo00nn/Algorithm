def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i,j in zip(participant, completion):
        if i != j:
            return i
    return participant[-1]


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
