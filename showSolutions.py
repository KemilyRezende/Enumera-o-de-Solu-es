def showSolutions(sol, var):
    a = 0
    b = 0
    min = 0
    vv = 0
    inv = 0

    # Encontra a solução ótima, quantidade de soluções viáveis e inviáveis
    for s in sol:
        if (s[var+1] == 0):
            vv += 1
            if (s[var] < min):
                min = s[var]
                a = b
        else:
            inv += 1
        b += 1
    b = 0

    # Imprime as soluções
    for s in sol:
        print("Solução: x = (", f"{s[0]:.2f}", end='')
        i = 1
        for i in range(var):
            print(",", f"{s[i]:.2f}", end = '')
        print(" ), z =", f"{s[var]:.2f}", end = '')
        if (b == a):
            print(", viável ==> ótima")
        else:
            if (s[var+1] == 0):
                print(", viável")
            else:
                print(", inviável")
        b += 1
    print("\nSoluções básicas viáveis:", vv)
    print("Soluções básicas inviáveis:", inv)