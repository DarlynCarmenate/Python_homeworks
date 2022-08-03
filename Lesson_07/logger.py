from dictionary import d

def dict_write():
    with open('dict.txt','w') as out:
        for key,val in d.items():
            out.write('{}:{}\n'.format(key,val))
    out.close()

def dict_read():
    d2 = {}
    with open('dict.txt', 'r') as inp:
        for i in inp.readlines():
            key,val = i.strip().split(':')
            d2[key] = val
        print(d2)
    inp.close()

