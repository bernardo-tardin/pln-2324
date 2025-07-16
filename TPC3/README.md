## TP3

### 🇵🇹

Este trabalho consiste na realização de um programa em Python que permite através de um ficheiro em formato _pdf_ criar uma página HTML.

Inicialmente, foi utilizado o comando _pdftotext_ no terminal para realizar a conversão do formato _.pdf_ para _.txt_. O uso de expressões regulares através da biblioteca importada _re_ foi fundamental para realizar as alterações necessárias no ficheiro a fim de conseguir uma correta visualização dos pares termo-designação.

Após a obtenção de uma lista com os pares termo-designação corretamente definidos, o ficheiro HTML passou a ser criado a partir da iteração dos dados presentes nesta lista. 

A fim de expandir as propriedades da página HTML, foi criado um ficheiro _style.css_ que é referenciado na seção _<head>_ do ficheiro HTML.

### 🇬🇧

This work consists of a developing a Python program that geneates a HTLM page from a PDF file.

First, the command _pdftotext_ was used in the terminal to convert _.pdf_ format to _.txt_. The use of regular expressions, throught the imported _re_ library, was essential to apply the necessary modifications to the file text in order to correctly extract the term-designation pairs.

Once a list with properly definied term-designation pairs was obtained, the HTML file was created by iterating over the data in this list.

To enhance the appearance of the HTML page, a file called _style.css_ was created and linked in the _<head>_ section of the HTML file.
