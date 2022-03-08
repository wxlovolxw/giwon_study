import sys

    a = sys.argv[1]
    b = sys.argv[2]


f = open(a, 'r')
tab_text = f.read()
f.close()

space_txt = tab_text.replace("\t"," "*4)

f = open(b,'w')
f.write(space_txt)
f.close()