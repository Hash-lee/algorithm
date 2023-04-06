for t in range(10):
    num = input()
    word = list(input())
    text = input()

    lt = len(text)
    lw = len(word)

    cnt = 0
    for i in range(lt - lw + 1):
        tmp = 0
        if text[i] == word[0]:
            tmp += 1
            for j in range(1, lw):
                if text[i + j] == word[j]:
                    tmp += 1
            if tmp == lw:
                cnt += 1