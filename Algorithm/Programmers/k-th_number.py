array= [1, 5, 2, 6, 3, 7, 4]

commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

sol = []
for command in commands :
    array_new = sorted(array[command[0]-1:command[1]])
    sol.append(array_new[command[2]-1])

print(sol)