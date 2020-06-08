def solution(n, lost, reserve):
    U = list(range(1, n+1))       #체육수업을 들을 수 있는 학생
    L = list(set(lost) - set(reserve))  #체육복을 잃어버린 학생
    R = list(set(reserve) - set(lost))  #여벌의 체육복
                                        #집합 자료형으로 오름차순 정렬 + 중복 제거
    for a in L:

        if (a + 1) not in R and (a - 1) not in R:
            U.remove(a)

        #체육복을 잃어버린 학생의 앞번호와 뒷번호 학생에게 여벌의 체육복이 있는지 확인 없을시 체육수업에서 제외

        elif (a + 1) in R and (a - 1) not in R:
            R.remove(a + 1)

        #뒷번호 학생에게만 여벌의 체육복이 있다면 해당 체육복 리스트에서 제거

    return len(U)

print(solution(5, [2, 4], [1, 3, 5]))

