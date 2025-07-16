## TPC6

### 🇵🇹

Este trabalho consiste na criação de website que permite visualizar de forma intuitiva os conceitos médicos e suas respetivas traduções.

Para facilitar o desenvolvimento, o ficheiro *conceitos_trad.json* anteriormente criado no TPC5 foi modificado para que cada chave presente no dicionário o valor correspondente seja um dicionário com as chaves "descricao" e "traducao", conforme pode ser visualizado na imagem abaixo:

![ficheiro conceitos_trad](ficheiro.png)

Foi utilizado o *framework* Flask para o desenvolvimento do website conforme pode ser visualizado no ficheiro *dicionarioMedico.py*. Foram criadas diferentes funções com suas respetivas *routes* permitindo que a interface criada seja dinâmica de forma com que o utilizador possa adicionar novo conceito com sua respetiva definição e tradução, editar uma descrição, adicionar uma nova tradução e pesquisar um determinado conceito.

Em relação à parte estética das páginas criadas foi utilizado o *framework* Bootstrap que utiliza as linguagens HTML, CSS e JavaScript. Os _templates_ criados estão presentes na diretoria "templates" e são chamados através das funções presentes no ficheiro *dicionarioMedico.py*. A fim de facilitar o desenvolvimento das páginas, foi criado um *template* base denominado "layout.html" que é retornado em todos os demais *templates* através de *{% extends layout.html %}*.

Abaixo estão alguns *screenshots* de como o website foi desenvolvido:

![home](home.png)

![lista conceitos](listaConceitos.png)

![adicionar conceito](adicionarConceito.png)

![conceito](conceito.png)

![editar descricao](editarDescricao.png)

![adicionar traducao](adicionarTraducao.png)

![apagar conceito](apagarConceito.png)

### 🇬🇧

This project consists of creating a website that allows for intuitive visualisation of medical concepts and their respective translations.

To facilitate development, the conceitos_trad.json file previously created in TPC5 was modified so that each key in the dictionary corresponds to a value that is itself a dictionary containing the keys "descricao" (description) and "traducao" (translation), as shown in the image below:

![ficheiro conceitos_trad](ficheiro.png)

The Flask framework was used to develop the website, as implemented in the dicionarioMedico.py file. Several functions were created with their corresponding routes, allowing the interface to be dynamic so that the user can add a new concept with its definition and translation, edit an existing description, add a new translation, and search for a specific concept.

For the visual styling of the pages, the Bootstrap framework was used, which relies on HTML, CSS, and JavaScript. The templates are stored in the "templates" directory and are called from the functions in dicionarioMedico.py. To streamline the development of the pages, a base template named layout.html was created, which is extended in all other templates using {% extends 'layout.html' %}.

Below are some screenshots showing how the website was developed:

![home](home.png)

![lista conceitos](listaConceitos.png)

![adicionar conceito](adicionarConceito.png)

![conceito](conceito.png)

![editar descricao](editarDescricao.png)

![adicionar traducao](adicionarTraducao.png)

![apagar conceito](apagarConceito.png)


