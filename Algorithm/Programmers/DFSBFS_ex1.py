from collections import deque

def similarity(a,b) :
    count = 0
    for i in range(len(list(a))) :
        if list(a)[i] != list(b)[i] :
            count += 1
    return count

def solution(begin, target, words) :

    words.append(begin)
    graph = {}

    for word in words:
        graph[word] = set([x for x in words if similarity(word, x) == 1])

    visited = []

    queue = deque([begin])


    while queue :

        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))