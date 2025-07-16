## TPC8

### 🇵🇹

Este trabalho consiste no desenvolvimento e no aprimoramento de modelos de Word Embedding através da utilização da biblioteca Gensim com auxílio da técnica Word2Vec em que as palavras passam a ser representadas como vetores.

Foi disponibilizado dois ficheiros de texto correspondentes aos livros da saga Harry Potter (Harry Potter Câmara Secreta e Harry Potter e a Pedra Filosofal) em que através da função *tokenize* do Gensim foi possível obter os tokens presentes em cada livros e armazená-los em listas para que os modelos sejam treinados.

Sendo assim, para o livro Harry Potter Câmara Secreta, os tokens foram armazenados na lista *tokens1* e então foram os criados o modelo *model1_1* com vector_size = 100, epochs = 5 e sg = 1 e o modelo *model1_2* com com vector_size = 300, epochs = 20 e sg = 0. De acordo com as respostas obtidos para as funções de similiaridade, *no match* e analogias, foi possível verificar que o modelo *model1_1* apresentou melhor resultado.

Para o livro Harry Potter e a Pedra Filosofal, foi realizado o mesmo procedimento, ou seja, o armazenamento dos tokens na lista *tokens2* e a criação dos modelos *model2_1* e *model2_2*. Igualmente foi possível notar que o modelo com vector_size = 100, epochs = 5 e sg = 1 apresentou melhores resultados.

Na tentativa de produzir um melhor modelo, foi então criada uma nova lista de tokens, *tokens3*, que corresponde a junção das outras duas listas. Os modelos gerados a partir desta lista foi o que apresentou os piores resultados comparativamente aos demais.

### 🇬🇧

This project focuses on the development and refinement of Word Embedding models using the Gensim library and the Word2Vec technique, in which words are represented as vectors.

Two text files were provided, corresponding to books from the Harry Potter series (Harry Potter and the Chamber of Secrets and Harry Potter and the Philosopher’s Stone). Using Gensim's tokenize function, the tokens from each book were extracted and stored in separate lists for model training.

For Harry Potter and the Chamber of Secrets, the tokens were stored in the list tokens1, and two models were created: model1_1 with vector_size = 100, epochs = 5, and sg = 1; and model1_2 with vector_size = 300, epochs = 20, and sg = 0. Based on the results from similarity, doesn’t match, and analogy functions, model1_1 showed better performance.

The same procedure was followed for Harry Potter and the Philosopher’s Stone, storing the tokens in the list tokens2, and creating model2_1 and model2_2. Again, the model with vector_size = 100, epochs = 5, and sg = 1 produced better results.

In an attempt to create an improved model, a third token list, tokens3, was created by combining the two previous lists. However, the models trained using tokens3 performed worse than the individual models.
