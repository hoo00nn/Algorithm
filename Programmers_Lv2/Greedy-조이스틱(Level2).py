import string


def solution(name):
    answer = 0
    alpha = dict()
    cursor = 0

    for idx, item in enumerate(string.ascii_uppercase):
        alpha[item] = idx

    for idx, item in enumerate(name):
        if item == 'A':
            continue
        else:
            if alpha[item] > 12:
                answer += len(alpha) - alpha[item]
            else:
                answer += alpha[item]

            if idx - cursor > cursor + len(name) - idx:
                answer += cursor + len(name) - idx;
                cursor = idx
            else:
                answer += idx - cursor
                cursor = idx
    print(answer)
    return answer

solution('JJAJAAAAAAAAAJ')