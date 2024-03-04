#Exercicio 1
def rev(string):
    return str[::-1]



#Exercicio 2
def countA(string):
    num_A = 0
    num_a = 0
    for letra in string:
        if letra == "A":
            num_A += 1
        elif letra == "a":
            num_a += 1
    return (num_A, num_a)

#Outra solucao
def countA2(string):
    num_a = [x for x in string if x == "a"]
    num_A = [x for x in string if x == "A"]
    return (len(num_a),len(num_A))



#Exercicio 3
def countVogais(string):
    num_Vogais = 0
    for letra in string:
        if letra in 'aeiouAEIOU':
            num_Vogais += 1
    return num_Vogais



#Exercicio 4
def lowercase(string):
    return string.lower()



#Exercicio 5
def uppercase(string):
    return string.upper()



#Exercicio 6
def capicua(string):
    return string == string[::-1]



#Exercicio 7
def balanc(string1,string2):
    balanceada = True
    for letra in string1:
        if letra not in string2:
            balanceada = False
    return balanceada



#Exercicio 8
def ocorrencia(string1,string2):
    return string2.count(string1)

#Outra solucao
def ocorrencia2(string1,string2):
    i = 0
    count = 0
    while i < len(string2):
        if string1 == string2[i:len(string1)+i]:
            count += 1
        i += 1
    return count



#Exercicio 9
def anagrama(string1,string2):
   return sorted(list(string1)) == sorted(list(string2))




#Exercicio 10 

#Abertura e leitura do ficheiro
file = open('CIH _Bilingual _Medical _Glossary_English-Spanish.txt')
text = file.read()

#Tranformação de todo o texto do ficheiro em letras minúsculas
text = text.lower()

#Remoção de símbolos, números e acentos
numbers = [x for x in range (0,10)]
acentos_a = ["á","ã","à","â"]
acentos_e = ["é","è"]


for crc in text:
    if not crc.isalnum():
        text = text.replace(crc," ")
for num in numbers:
    text = text.replace(str(num)," ")
for a in acentos_a:
    text = text.replace(a,"a")
for e in acentos_e:
    text = text.replace(e,"e")
text = text.replace("ñ","n")
text = text.replace("ó","o")
text = text.replace("í","i")
text = text.replace("ú","u")


#Divisão do texto em palavras únicas
tokens = text.split()
tokens = list(set(tokens))

#Criação do dicionário
anagramas = {}
for palavra in tokens:
    if len(palavra) > 1: #Garantir que a palavra não seja somente uma letra
        lista = sorted(list(palavra)) #Ordenação dos caracteres da palavra
        new_palavra = ''
        for x in lista:
            new_palavra += x
        if new_palavra not in anagramas.keys():
            anagramas[new_palavra] = [palavra]
        else:
            anagramas[new_palavra].append(palavra)

#Criação de um novo dicionário a partir do anterior de forma com que o novo somente possua anagramas
new_anagramas = {}
for pair in anagramas.items():
    if len(pair[1]) > 1:
        new_anagramas[pair[0]] = pair[1]

print(new_anagramas) 


#

    


