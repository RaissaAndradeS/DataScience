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


 ### <center> Tipagem </center>

 Há uma diferença entre arrays e listas e essa diferença é a sua tipagem. Listas podem ter vários tipos de dados (string, inteiros, floats...), arrays tendem a possuir tipagem fixa e a tipagem pode ser modificada utilizando o método astype.

 ``` 
 array = np.array([1, 2, 3], dtype=np.uint8)
 array = array.astype("float")
 print(array.dtype, array)
 ```


### <center> Indexação </center>

Arrays podem ser indexados tais quais elementos de Python.

```
array = np.arange(1, 10)
matriz = np.random.normal(1, 2, (3, 3))

print(array)
print(matriz)
```

para acessar o elemento 1 

```
array[0]
```

### <center> Mutabilidade </center>

Distindo de listas, arrays são objetos __imutáveis__ em tamanho e tipo, só dá pra mudar se criar um novo array.

Arrays são passados como referência em função, de forma que qualquer alteração no array feito dentro de uma função será carregada para fora da mesma.
