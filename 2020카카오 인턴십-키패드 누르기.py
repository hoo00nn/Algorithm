def keypad(pad):
    ret = dict()

    for i in range(len(pad)):
        for j in range(len(pad[i])):
            ret[pad[i][j]] = (j, i)

    return ret


def check(numbers, keypad, hand):
    left_cursor = keypad['*']
    right_cursor = keypad['#']
    ret = ''

    for i in numbers:
        if i == 1 or i == 4 or i == 7 or i == '*':
            left_cursor = keypad[i]
            ret += 'L'
        elif i == 3 or i == 6 or i == 9 or i == '#':
            right_cursor = keypad[i]
            ret += 'R'
        else:
            left = abs(left_cursor[0] - keypad[i][0]) + abs(left_cursor[1] - keypad[i][1])
            right = abs(right_cursor[0] - keypad[i][0]) + abs(right_cursor[1] - keypad[i][1])
            if left == right:
                if hand == 'left':
                    left_cursor = keypad[i]
                    ret += 'L'
                else:
                    right_cursor = keypad[i]
                    ret += 'R'
            elif left < right:
                left_cursor = keypad[i]
                ret += 'L'
            elif right < left:
                right_cursor = keypad[i]
                ret += 'R'

    return ret


def solution(numbers, hand):
    pad = [[1, 2, 3], [4, 5, 6, ], [7, 8, 9], ['*', 0, '#']]
    key = keypad(pad)
    answer = check(numbers, key, hand)

    return answer