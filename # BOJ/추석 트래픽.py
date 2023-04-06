def solution(lines):
    start = []
    end = []
    for line in lines:
        splt = line.split()
        h, m, s = map(float, splt[1].split(":"))
        t = h * 3600000 + m * 60000 + s * 1000
        end.append(t)
        spend = float(splt[2][:-1]) * 1000
        start.append(t - spend + 1)

    start.sort()
    end.sort()

    num = len(lines)
    plus = 0
    minus = 0

    mx = -1
    while minus < num and plus < num:
        s = 0
        for x in start[plus:]:
            if x < start[plus] + 1000:
                s += 1
            else:
                break

        if start[plus] <= end[minus]:
            plus += 1
        else:
            minus += 1
        on = plus - minus + s
        if on > mx:
            mx = on

    answer = mx
    return answer


ans3 = solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
2002 - 4001
5001 - 7000


print(ans3)
