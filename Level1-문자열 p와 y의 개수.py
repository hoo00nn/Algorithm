def solution(s):
    s = s.lower()

    return True if s.count('y') == s.count('p') else False