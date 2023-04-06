t = int(input())
l = [2, 3, 5, 7, 11]
for i in range(t):
    n = int(input())
    r = [0]*5
    for s in range(5):
    	while n%l[s] == 0:
            n = n/l[s]
            r[s] += 1 
    
    print('#{}'.format(i+1),r[0],r[1],r[2],r[3],r[4])