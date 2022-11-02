
import sys


def string_to_bitmask(string: str):
    bit_mask = 0b0
    set_str = set(string)
    for s in set_str:
        bit_mask |= 1 << (ord(s) - ord("a"))
    bit_words.append(bit_mask)


def compare_bitmasks(bit_mask, cnt=5, idx=1):
    if cnt < M:
        for i in range(idx, 26):
            if bit_mask & 1 << i == 1 << i:
                continue
            copied = bit_mask
            copied |= 1 << i
            compare_bitmasks(copied, cnt + 1, i + 1)
    else:
        counts = 0
        for bit_word in bit_words:
            if bit_mask | bit_word == bit_mask:
                counts += 1
        global answer
        if answer < counts:
            answer = counts
        return


N, M = map(int, sys.stdin.readline().split())
if M < 5:
    print(0)
elif M == 26:
    print(N)
else:
    bit_words = []
    for _ in range(N):
        string_to_bitmask(sys.stdin.readline().rstrip())
    answer = 0
    bit_mask = 0b0
    for s in ["a", "n", "t", "i", "c"]:
        bit_mask |= 1 << (ord(s) - ord("a"))
    compare_bitmasks(bit_mask)
    print(answer)
