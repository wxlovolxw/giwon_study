def stdout(S) :
    S_list = list(S)

    result = []
    count = 1

    for i, num in enumerate(S_list):
        if i < len(S_list) - 1:
            if S_list[i] == S_list[i + 1]:
                count += 1
            else:
                rep = str((count, int(num)))
                result.append(rep)
                count = 1
        else:
            rep = str((count, int(num)))
            result.append(rep)

    return(" ".join(result))

stdin = input()

print(stdout(stdin))