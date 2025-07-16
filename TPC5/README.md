## TPC5

### 🇵🇹

Este trabalho consiste no aperfeiçoamento do código criado na aula que realiza o etiquetamento de termos e gera um ficheiro HTML. Para tal, foi fornecido um ficheiro denominado *termos_traduzidos.txt* que apresenta uma lista de termos em português com as respetivas traduções em inglês separadas por um @. Portanto, o objetivo é alterar o campo title da tag <a> já desenvolvida com a introdução da tradução antes da descrição.

Foi criado um ficheiro termos_ingles.py que realiza a extração dos termos e suas respetivas traduções através da expressão regular r'(.+)@(.+)' pela função _findall_, retornando uma lista de tuplos (portugues_ingles) em que o primeiro elemento de cada tuplo é o termo em português e o segundo, em inglês. A lista criada é, então, convertida num dicionário. O código desenvolvido neste ficheiro permite, no fim, criar um ficheiro json com o dicionário criado em que as chaves são os termos em português e os valores, os termos em inglês.

Em relação ao ficheiro etiquetador.py, foi adicionada a abertura do ficheiro *conceitos_ingles.json* a fim de extrair o dicionário. Na função _etiquetador_ anteriormente desenvolvida, foram adicionadas novas condições if/else que verificam se os termos analisados estão presentes ou não nos dicionários *termos_ingles* e *conceitos_mini*. Caso o termo a ser analisado esteja presente em ambos, é adicionada à tag <a> a tradução em inglês antes da descrição. 

Foi solicitado que, ao adicionar a tradução, tivesse uma quebra de linha entre a tradução e a descrição, portanto, foi necessário deslocar a linha de código *texto = re.sub(r'\n','<br>',texto)* para antes da função etiquetador para que não ocorresse a substituição do "\n".

### 🇬🇧

This work consists of improving the code developed in class that performs term tagging and generates an HTML file. For this purpose, a file named termos_traduzidos.txt was provided, containing a list of Portuguese terms along with their English translations, separated by an @ symbol. The goal is to modify the title attribute of the already implemented <a> tag by adding the English translation before the description.

A script named termos_ingles.py was created to extract the terms and their respective translations using the regular expression r'(.+)@(.+)' with the findall function. This returns a list of tuples (portuguese_english), where the first element is the Portuguese term and the second is its English translation. The list is then converted into a dictionary. The code in this script generates a JSON file containing the dictionary, where the keys are the Portuguese terms and the values are the corresponding English terms.

In the etiquetador.py file, code was added to open the conceitos_ingles.json file in order to load the dictionary. In the previously developed etiquetador function, new if/else conditions were introduced to check whether the analysed terms are present in both the termos_ingles and conceitos_mini dictionaries. If a term is found in both, the English translation is added to the <a> tag before the description.

As it was required to insert a line break between the translation and the description, the line of code texto = re.sub(r'\n','<br>', texto) was moved to before the etiquetador function to prevent the replacement of "\n" at an inappropriate stage.
