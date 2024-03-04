## Trabalho de Casa 3

Este trabalho consiste na realização de um programa em Python que permite através de um ficheiro em formato _pdf_ criar uma página HTML.

Inicialmente, foi utilizado o comando _pdftotext_ no terminal para realizar a conversão do formato _.pdf_ para _.txt_. O uso de expressões regulares através da biblioteca importada _re_ foi fundamental para realizar as alterações necessárias no ficheiro a fim de conseguir uma correta visualização dos pares termo-designação.

Após a obtenção de uma lista com os pares termo-designação corretamente definidos, o ficheiro HTML passou a ser criado a partir da iteração dos dados presentes nesta lista. 

A fim de expandir as propriedades da página HTML, foi criado um ficheiro _style.css_ que é referenciado na seção _<head>_ do ficheiro HTML.