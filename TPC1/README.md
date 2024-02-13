## Trabalho de Casa 1

Este trabalho consiste na realização de exercícios de revisões de tópicos em Python. Do exercício 1 ao 9 foram criadas as funções solicitadas no enunciado. Para os exercícios 2 e 8, foram desenvolvidas 2 propostas de solução.

Para o exercício 10, foi solicitada a criação de um dicionário que possua a tabela de classes de anagramas a partir de um ficheiro de texto. Portanto, após a abertura e a leitura do ficheiro, foi a realizada a preparação do texto com a remoção de símbolos, números e acentos presentes. No dicionário _anagramas_, a chave corresponde as palavras presentes no texto em que as letras estão ordenadas alfabeticamente e o valor corresponde a lista de palavras que possuem exatamente as mesmas letras da chave, ou seja, são anagramas. 
Para garantir que o dicionário apresente somente as palavras que são anagramas, foi necessário criar um novo dicionário *new_anagramas* uma vez que o Python não permite alterar o tamanho do dicionário _anagramas_ enquanto está a iterar sob ele.