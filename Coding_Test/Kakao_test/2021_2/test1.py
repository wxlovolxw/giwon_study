
def solution(s) :

    s_list = list(s)
    answer =[]

    for i, word in enumerate(s_list):

        try :
            if word == 'z':
                answer.append(0)
                del s_list[i:i + 3]

            elif word == 'o':
                answer.append(1)
                del s_list[i:i + 2]

            elif word == 't' and s_list[i + 1] == 'w':
                answer.append(2)
                del s_list[i:i + 2]

            elif word == 't' and s_list[i + 1] == 'h':
                answer.append(3)
                del s_list[i:i + 4]

            elif word == 'f' and s_list[i + 1] == 'o':
                answer.append(4)
                del s_list[i:i + 3]

            elif word == 'f' and s_list[i + 1] == 'i':
                answer.append(5)
                del s_list[i:i + 4]

            elif word == 's' and s_list[i + 1] == 'i':
                answer.append(6)
                del s_list[i:i + 2]

            elif word == 's' and s_list[i + 1] == 'e':
                answer.append(7)
                del s_list[i:i + 4]

            elif word == 'e':
                answer.append(8)
                del s_list[i:i + 4]

            elif word == 'n':
                answer.append(9)
                del s_list[i:i + 3]

            elif word in ['0','1','2','3','4','5','6','7','8','9'] :
                answer.append(int(word))

        except IndexError : pass

    answer = [str(x) for x in answer]
    return int("".join(answer))


print(solution("one4seveneight"))