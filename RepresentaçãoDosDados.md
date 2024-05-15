## Representação dos Dados 

Foi carregado na memória RAM um dataframe, o dataframe é uma estrutura de dados que representa uma tabela, pode ser definido por linhas e colunas nomeadas que permitem acessar o conteúdo de cada célula "dado".

Isso sendo computacional, cada coluna de uma dataframe é representada por um outro elemento chamado "Série" e cada série são uma coluna de informação, é uma informação nomeada, e tem informação pra cada série.

Séries são arrays que são representados pela biblioteca Numpy.

### <center> Numpy </center>

Arrys são objetos que armazenam estrutura sequenciais de dados de tipo e tamanhos determinado. 

- criação de array

```

    array = np.array([1, 2, 3, 4, 5])
    array

```

### Características

 - dtype: O tipo de dados do array
 - shape: O tamanho do array em linhas e colunas
 - size: O tamanho do array em quantidade de elementos
 - itemsize: O consumo de memória de cada elemento do array (em bytes)
 - strides: Uma distancia em bytes entre os elementos armazenados na memória