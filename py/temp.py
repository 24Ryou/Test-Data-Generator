""" from unidecode import unidecode
#   bnum - bname - wnum - enum - gnum - anum - address - contract - manager - parking - warehouse


with open("./files/txt/temp.txt", 'r' , encoding='utf8') as f:
    c = f.read().splitlines()
    print(c)
    zcode = []
    state = []
    for x in range(1,len(c),2) :
        zcode.append(c[x])
    
    for x in range(0,len(c),2) :
        state.append(c[x])
    
print(zcode)
with open("./files/txt/zcode.txt", 'w' , encoding='utf8') as f:
    for x in zcode :
        f.write(unidecode(x+"\n"))
print(state)
with open("./files/txt/state.txt", 'w' , encoding='utf8') as f:
    for x in state :
        f.write(x+"\n") """


import rstr

a = rstr.xeger(r'[0-9]{8}')
print(a)