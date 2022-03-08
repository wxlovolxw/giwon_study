

def solution(needs, r) :


    needs_comp = [x for x in needs if sum(x) <= r]

    return needs_comp




print([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ], 2)