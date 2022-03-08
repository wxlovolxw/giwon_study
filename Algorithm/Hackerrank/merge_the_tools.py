from collections import OrderedDict

def merge_the_tools(string, k) :

    list_s = list(string)

    u = [list_s[i * k:(i + 1) * k] for i in range((len(list_s) + k - 1) // k)]

    t = []
    for num, ui in enumerate(u) :

        ex_list = list(OrderedDict.fromkeys(ui))

        t.append(''.join(ex_list))

        print(t[num])
