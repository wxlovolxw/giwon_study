def g(k):
    numlist = list(map(int, k))
    if k > 1000:
        result = int(k) + numlist[0] + numlist[1] + numlist[2] + numlist[3]
    elif k > 100:
        result = int(k) + numlist[0] + numlist[1] + numlist[2]
    elif k > 10:
        result = int(k) + numlist[0] + numlist[1]
    else:
        result = 2

print(g(2341))