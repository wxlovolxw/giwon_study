
def solution(genres, plays) :

    genre = {}
    count = 1

    for i in genres :
        if i not in genre:
            genre[i] = count
        else : genre[i] += 1

    a = list(map(lambda x,y : [genre[y],plays[x],x], enumerate(plays),genres))

    return a

print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],[500, 600, 150, 800, 2500]))