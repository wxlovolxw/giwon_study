
def solution(gift_cards,wants) :

    wants_tup = list(set(list(map(lambda x: (x, wants.count(x)), wants))))

    count = 0

    for i in wants_tup :

        count += max(i[1] - gift_cards.count(i[0]), 0)

    return count


print(solution([4, 5, 3, 2, 1],[2, 4, 4, 5, 1]))