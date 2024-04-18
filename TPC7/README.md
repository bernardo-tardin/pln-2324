## Trabalho de Casa 7

Este trabalho consiste no aprimoramento do website desenvolvido no TPC6 com a inserção de permissão de adicionar e apagar novos conceitos, visualização dos conceitos numa tabela e adição de uma página de busca.

Como a página web desenvolvida no TPC6 já possuía a permissão de adicionar e apagar conceitos e, também, editar descrição e adicionar nova tradução, a estrutura do ficheiro *dicionarioMedico.py* foi mantida. Ou seja, foi utilizado o método POST, juntamente com a função *request.form*, para que essas funcionalidades fossem implementadas. No entanto, para que a informação da base de dados, neste caso, um ficheiro JSON, seja consistente, foi necessário que para cada alteração realizada o seguinte segmento de código é chamado:

`with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
        json.dump(conceitos, file, ensure_ascii=False, indent=4)`

Para a construção da página de pesquisa, foi desenvolvida a função *pesquisa()* que, semelhante ao o que estava implementado no TPC6, utiliza a função *request.form.get* para obter o texto inserido no campo input com nome "search". Caso o texto a ser pesquisado seja encontrado nos conceitos ou nas descrições, é retornado um dicionário denonimado *resultados* em que as chaves são os conceitos e os valores, as descrições, permitindo atualizar a lista de conceitos visível ao utilizador. Caso contrário, retorna para uma página de erro default que indica que o conceito que está sendo procurado não foi encontrado. 

Em relação à página de erro, foi utilizado um layout pré-feito que é indicado no template *error.html* através de tags <link> com propriedade rel="stylesheet".

Para a tabela de dados, foi necessário recorrer à utilização da linguagem JavaScript através da utilização da biblioteca jQuery. Criou-se, então, uma diretoria denominada "static" que possui o ficheiro *script1.js* em que chama a função *DataTable()* disponível na biblioteca. Para a implementação da página, foi criado o template *table.html* que através de um ciclo *for* adiciona novas linhas à tabela de acordo com os dados presentes no dicionário *conceitos*. Como a estrutura do ficheiro JSON permite que haja conceitos sem as respetivas traduções, estabeleceu-se uma condição *if* para que, no caso destes conceitos, seja impresso o texto "Sem Tradução".

Abaixo está um vídeo que demonstra a utilização da página web desenvolvida:

[![](video.mov)]
