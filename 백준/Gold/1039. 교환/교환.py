def exchange(arr, k):
    dic[k] += [arr]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            nrr = arr[:]
            if i != 0 or nrr[j] != '0':
                nrr[i], nrr[j] = nrr[j], nrr[i]
                if (k > 0) and (not nrr in dic[k-1]):
                    exchange(nrr, k-1)

N, K = input().split()
K = int(K)
num = (" ".join(N)).split()
dic = {}
for i in range(K+1):
    dic[i] = []
exchange(num, K)

nums = dic[0]
if nums:
    nums.sort()
    print(int("".join(nums[-1])))
else:
    print("-1")