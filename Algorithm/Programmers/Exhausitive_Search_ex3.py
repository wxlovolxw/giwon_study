def solution(brown, yellow):
    sum = brown + yellow
    sqrt_sum = round(pow(sum, 1 / 2)) + 1

    for i in range(3, sqrt_sum):
        if sum % i == 0:
            x = i
            y = sum // i

            if (x * 2) + (y * 2) - 4 == brown:
                return [max(x, y), min(x, y)]

print(solution(8,1))