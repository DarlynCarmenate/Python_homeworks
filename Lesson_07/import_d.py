from dictionary import d

def imp_data(d):
    for i in range(10, 20):
        d[i] = input('write')
        if not d[i]:
            del d[i]
            break
    return d
