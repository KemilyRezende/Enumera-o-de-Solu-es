import numpy as np
import itertools as it

def enumerateSolutions(var, res, fun, matrix, values):
    # Cria um vetor com valores de 0 à n para fazer as combinações de variáveis a serem zeradas
    variables = []
    for i in range(var):
        variables.append(i)

    # Gera as combinações
    comb = it.combinations(variables, (var-res))

    # Define um objeto do tipo np.array com os termos independentes das restrições
    v = np.array(values)

    # Armazena as soluções
    sol = []

    # Para cada combinação calcula os valores das variáveis não zeradas
    for c in comb:

        # Cria um objeto np.array com os coeficientes das restrições
        mtx = np.array(matrix)

        # Zera as colunas referentes às variáveis zeradas
        for j in c:
            mtx[:,j] = 0

        # Deleta as colunas zeradas para deixar a matriz quadrada
        mtx = np.delete(mtx, c, axis=1)

        # Tenta resolver linearmente, dessa forma é possível administrar casos em que o sistema analisado é impossível
        try:
            # Resolve o sistema linear para as variáveis não zeradas
            r = np.linalg.solve(mtx, v)

            # Valores das variáveis x1-xn
            x = []

            # index para o vetor de valores das variáveis
            id = 0

            # Valores negativos na solução
            ng = 0

            for i in range(var):
                # Se o valor refere se a uma variável zerada armazena 0
                if i in c: 
                    x.append(0)
                # Caso contrário armazena o devido valor
                else:
                    x.append(r[id])
                    # Se algum valor é negativo armaena -1 na variável ng
                    if (r[id] < 0): 
                        ng = -1
                    # Incrementa id para armazenar o valor das variáveis no local correto
                    id += 1
            # Calcula o valor da função objetivo
            z = 0
            for i in range(var):
                z += x[i]*fun[i]
            
            # Armazena o valor da função objetivo
            x.append(z)
            
            # Armazena a viabilidade (-1 = INVIÁVEL, 0 = VIÁVEL)
            x.append(ng)
            
            # Armazena a solução
            sol.append(x)

        # Ao encontrar um SI simplesmente o ignora e continua oprograma, visto que o mesmo não é uma solução básica
        except np.linalg.LinAlgError as e:
            continue
    
    # Retorna o conjunto de soluções
    return sol