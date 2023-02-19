def solution(sizes):
    big = []
    small = []

    for size in sizes:
        big.append(max(size))
        small.append(min(size))

    answer = max(big) * max(small)

    return answer
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))