def solution(phone_book):
    answer = True

    for i in phone_book:
        count = 0
        for j in range(0, len(phone_book)):
            check = phone_book[j]
            if i == check[0:len(i)]:
                count += 1
        if count > 1:
            answer = False
            return answer
    answer = True
    return answer

solution(["119", "97674223", "1195524421"])
