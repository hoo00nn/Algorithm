def solution(bridge_length, weight, truck_weights):
    answer = 0
    isCrossBridge = []
    curTime = []

    while truck_weights:
        answer += 1
        if curTime:
            if curTime[0] + bridge_length == answer:
                del isCrossBridge[0]
                del curTime[0]
        if weight - sum(isCrossBridge) >= truck_weights[0]:
            isCrossBridge.append(truck_weights[0])
            curTime.append(answer)
            del truck_weights[0]
    answer = curTime[-1] + bridge_length
    return answer


solution(2, 10, [7, 4, 5, 6])
