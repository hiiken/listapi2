n1 = int(input())

cedulas = [33, 13, 8, 7, 1]

def calculaDinheiro(n1, array):
    qntd = []
    for c in range(0, len(array)):
        if(n1 // array[c] != 0):
            vx = n1 // array[c]
            n1 -= (vx*array[c])
            qntd.append(vx)
        else:
            qntd.append(0)
            continue

    return qntd


listaCedulas = calculaDinheiro(n1, cedulas)

for i in range(0, len(listaCedulas)):
    print("{} JabuticabaCoin(s) de OZ$ {}".format(listaCedulas[i], cedulas[i]))