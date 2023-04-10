def solution(s):
    sets = sorted(map(lambda x: set(map(int, x.split(","))), s[2:-2].split("},{")), key=lambda x: len(x))
    answer = [list(sets[x] - sets[x-1])[0] if x else list(sets[x])[0] for x in range(len(sets))]
    return answer