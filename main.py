import input
import enumerateSolutions
import showSolutions

def main():
    # Lê as variáveis
    var, res, fun, matrix, values = input.input()

    # Calcula as soluções
    solucoes = enumerateSolutions.enumerateSolutions(var, res, fun, matrix, values)
    
    # Mostra as soluções
    showSolutions.showSolutions(solucoes, var)
                
if __name__ == "__main__":
    main()
