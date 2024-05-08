# Enumerameração de Soluções

O projeto compromete-se a enumerar soluções básicas, viáveis e inviáveis, de problemas de programação linear de minimização.

## Tecnologias

### Python

A linguagem foi escolhida devido a simplicidade de escrita e ao enorme grupo de ferramentas disponibilizadas pelas bibliotecas (`NumPy` e `itertools`, nesse projeto) que facilitam o desenvolvimento da solução e a tornam mais precisa.

### Bibliotecas
- `NumPy:` fornece suporte para arrays e matrizes multidimensionais, além de funções matemáticas para operar nesses arrays.
- `itertools:` fornece ferramentas eficientes para criar iteradores para gerar e manipular combinações, permutações e outras operações sobre iteráveis.
- `sys:` fornece acesso a algumas variáveis e funções que interagem fortemente com o interpretador Python.

## Estrutura

O código é dividido em 4 arquivos para manter a organização e legibilidade.
- `input.py:` Responsável por gerenciar a entrada de dados, incluindo a leitura do arquivo de entrada e o processamento das informações necessárias para a resolução do problema.
- `enumerateSolutions:` Calcula todas as soluções possíveis para o problema de programação linear, distinguindo entre soluções viáveis e inviáveis.
- `showSolutions:` Determina a solução ótima, contabiliza a quantidade de soluções viáveis e inviáveis, e exibe o conjunto completo de soluções.
- `main.py:` O ponto de entrada do programa, que coordena a execução das funcionalidades definidas nos outros arquivos.

## Execução

Para executar o programa é necessário o seguinte comando:

```bash
python3 main.py arquivo_de_entradas.txt
```
Este comando iniciará o processo de resolução do problema de programação linear, utilizando as informações contidas no arquivo de entradas fornecido como argumento.
