# Projeto safeLevadas

This README is also available in English. Click here

## Contexto

O projeto safeLevadas é desenvolvido no contexto do curso de Programação 2 (LTI) do Departamento de Informática da Faculdade de Ciências de Lisboa, no ano letivo 2023/2024. Este projeto tem como objetivo criar uma aplicação em Python 3 chamada safeLevadas, destinada a encontrar os percursos mais rápidos entre dois pontos na rede de levadas da ilha da Madeira, melhorando o suporte e resgate de caminhantes.

## Descrição

O safeLevadas é um software projetado para apoiar as equipas de resgate na determinação do percurso mais rápido entre dois pontos geolocalizados na rede de levadas da Madeira. Este sistema é essencial para auxiliar na rápida resposta a chamadas de socorro de caminhantes perdidos ou em perigo.
## Funcionalidades

    Entrada: O programa recebe dois ficheiros de entrada:
        inputFile1.txt: Ficheiro com a rede de levadas.
        inputFile2.txt: Ficheiro com pares de estações para as quais se deseja calcular os percursos mais rápidos.

    Saída: O programa gera um ficheiro de saída com os resultados dos percursos calculados:
        outputFile.txt: Ficheiro com os tempos de percurso e sequências de estações.

## Como Executar

Para executar o software, utilize o seguinte comando na linha de comandos:

```bash
python safeLevadas.py inputFile1.txt inputFile2.txt outputfile.txt
```
Certifique-se de que a ordem dos ficheiros de entrada é a correta.

inputFile1.txt -> Rede de levadas, no formato especificado.

inputFile2.txt -> Pares de estações para os quais se deseja calcular os percursos.
Exemplo de Estrutura de Entrada e Saída
Estrutura de inputFile1.txt
```less
#Id, Name, Connected:
A, Seixal, [(R, 15), (M, 8), (B, 12)]
C, Pico Ruivo, [(GJ, 32), (I, 5)]
D, Queimadas, [(Z, 18), (AC, 11)]
E, Ponta do Pargo, [(DW, 13)]
```

## Estrutura de inputFile2.txt

```less
Cedro - Queimada
Ponta do Pargo - Calheta
Queimada - Boavista
Areeiro – Pico Ruivo
Moinho - Rabacal
```

Estrutura de outputfile.txt

```less

# Cedro - Queimada
76, Cedro, Queimada
83, Cedro, Rabacal, Queimada
120, Cedro, Ponta do Sol, Areeiro, Queimada
# Ponta do Pargo - Calheta
Calheta out of the network
# Queimada - Boavista
89, Queimada, Ponta do Sol, Pico Ruivo, Boavista
# Areeiro – Pico Ruivo
Areeiro and Pico Ruivo do not communicate
# Moinho - Rabacal
56, Moinho, Areeiro, Rabacal
56, Moinho, Popias, Rabacal
98, Moinho, Rabacal
```

## Desenvolvimento do Software

O software é composto pelos seguintes módulos:
```less
    constants.py: Define as constantes necessárias.
    dateTime.py: Contém funções para lidar com formatos e operações com datas e tempos.
    infoFromFiles.py: Fornece funções para ler informações de ficheiros.
    planning.py: Contém funções para realizar a determinação dos percursos mais rápidos.
    infoToFiles.py: Oferece funções para escrever informações em ficheiros.
    safeLevadas.py: Programa principal que utiliza os módulos anteriores para realizar a aplicação safeLevadas.
```
## Contribuidores
```less
    Nome do Estudante 1
    Nome do Estudante 2
```
## Relatório de Implementação

Consulte o relatório de implementação (relGroupN.pdf) para obter detalhes sobre as contribuições individuais de cada membro do grupo, funcionalidades extra implementadas (se aplicável), funcionalidades não implementadas (se aplicável) e erros conhecidos (se aplicável).


