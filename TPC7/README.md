## TPC7

### 🇵🇹

Este trabalho consiste no aprimoramento do website desenvolvido no TPC6 com a inserção de permissão de adicionar e apagar novos conceitos, visualização dos conceitos numa tabela e adição de uma página de busca.

Como a página web desenvolvida no TPC6 já possuía a permissão de adicionar e apagar conceitos e, também, editar descrição e adicionar nova tradução, a estrutura do ficheiro *dicionarioMedico.py* foi mantida. Ou seja, foi utilizado o método POST, juntamente com a função *request.form*, para que essas funcionalidades fossem implementadas. No entanto, para que a informação da base de dados, neste caso, um ficheiro JSON, seja consistente, foi necessário que para cada alteração realizada o seguinte segmento de código é chamado:

`with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
        json.dump(conceitos, file, ensure_ascii=False, indent=4)`

Para a construção da página de pesquisa, foi desenvolvida a função *pesquisa()* que, semelhante ao o que estava implementado no TPC6, utiliza a função *request.form.get* para obter o texto inserido no campo input com nome "search". Caso o texto a ser pesquisado seja encontrado nos conceitos ou nas descrições, é retornado um dicionário denonimado *resultados* em que as chaves são os conceitos e os valores, as descrições, permitindo atualizar a lista de conceitos visível ao utilizador. Caso contrário, retorna para uma página de erro default que indica que o conceito que está sendo procurado não foi encontrado. 

Em relação à página de erro, foi utilizado um layout pré-feito que é indicado no template *error.html* através de tags <link> com propriedade rel="stylesheet".

Para a tabela de dados, foi necessário recorrer à utilização da linguagem JavaScript através da utilização da biblioteca jQuery. Criou-se, então, uma diretoria denominada "static" que possui o ficheiro *script1.js* em que chama a função *DataTable()* disponível na biblioteca. Para a implementação da página, foi criado o template *table.html* que através de um ciclo *for* adiciona novas linhas à tabela de acordo com os dados presentes no dicionário *conceitos*. Como a estrutura do ficheiro JSON permite que haja conceitos sem as respetivas traduções, estabeleceu-se uma condição *if* para que, no caso destes conceitos, seja impresso o texto "Sem Tradução".

Abaixo está um vídeo que demonstra a utilização da página web desenvolvida:

https://github.com/bernardo-tardin/pln-2324/assets/147925451/6e22330f-8f54-4a60-8815-b46c39d6f5a9

### 🇬🇧

This project consists of improving the website developed in TPC6 by adding permissions to insert and delete concepts, displaying the concepts in a table format, and implementing a search page.

Since the web application developed in TPC6 already allowed adding and deleting concepts, editing descriptions, and adding new translations, the structure of the dicionarioMedico.py file was maintained. That is, the POST method was used, along with the request.form function, to implement these features. However, to ensure data consistency in the database — in this case, a JSON file — the following code snippet is called whenever a change is made:

`with open("/Users/bernardomoraes/Documents/GitHub/pln2324/TPC5/conceitos_trad.json", "w", encoding="utf-8") as file:
        json.dump(conceitos, file, ensure_ascii=False, indent=4)`

To build the search page, the pesquisa() function was created. Similar to the implementation in TPC6, it uses request.form.get to retrieve the text entered in the input field named "search". If the search term is found in the concepts or descriptions, a dictionary named resultados is returned, where the keys are the concepts and the values are the descriptions, allowing the concept list visible to the user to be updated. Otherwise, a default error page is displayed indicating that the searched concept was not found.

For the error page, a pre-designed layout was used, specified in the error.html template through <link> tags with the rel="stylesheet" attribute.

To display the data in table format, JavaScript was used via the jQuery library. A directory named "static" was created containing the file script1.js, which calls the DataTable() function from the library. The template table.html was implemented, where a for loop adds new rows to the table based on the data stored in the conceitos dictionary. Since the JSON file structure allows for concepts without corresponding translations, a conditional if statement was added to display the text "No Translation" when applicable.

Below is a video demonstrating the use of the developed web page:

https://github.com/bernardo-tardin/pln-2324/assets/147925451/6e22330f-8f54-4a60-8815-b46c39d6f5a9



