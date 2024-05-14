### O que são dados? 

Dados são representações computacionais usadas para guardar um conteúdo quantificável associado a uma entidade ou evento.

- São informações que foram traduzidas em uma forma eficiente para movimentação ou processamento. 
- Os computadores representam dados, incluindo vídeo, imagem, sons e textos, como valores binários usando padrões de apenas dois números: 0 e 1
- Nessa era, todos os sistemas automatizados geram alguma forma de dados ou para fins de diagnóstico ou análise.
- Dados sozinhos não expressão signidicado algum, sendo apenas um conteúdo quantificável associado a alguma entidade ou evento.
- Os dados brutos podem ser arbitrários, não estruturados, ou mesmo em um formato que não é imediatamente adequado para processamento automatizado.


### O que mineração de dados? 

É o estudo da coleta, limpeza, processamento, análise e obtenção de insights de dados.

## <center> Processo de mineração </center>
 
#### 1. Aquisição 
#### 2. Limpeza e Processamento 
#### 3. Análise e modelagem 
#### 4. Apresentação e discussão 
#### 5. Conhecimento 



## <center> Mineração </center>

- Minereação de dados é a exploração e análise de dados para descobrir padrões ou regras que sejam significativos.
- A mineração de dados tem como objetivo:
    1. Peneirar muitas informações repetitivas de maneira organizada.
    2. Extrair informações relevantes e faça o melhor uso delas para melhores resultados.
    3. Acelerar o ritmo da tomada de decisões bem informada.
- Há múltiplos métodos que permitem encontrar padrões de dados como:
    1. Reconhecimento Automático de Padrões.
    2. Previsão dos resultados mais prováveis.
    3. Destaque os agrupamentos que ocorrem naturalmente.


## <center> Coleta de Dados </center>

- Coleta de dados é o processo de amostragem de sinais que medem as condições físicas do mundo real e convertem as amostras resultantes em valores numéricos digitais que podem ser manipulados por um computador. 
- Os sistemas de aquisição de dados normalmente convertem formas de ondas analõgicas em valores digitais para processamento.
- Componentes dos sistemas de aquisição de dados:
    - Sensores, para converter parâmetros físicos em sinais elétricos.
    - Circuito de condicionamento de sinal, para converter os sinais do sensor em uma forma que pode ser convertida em valores digitais.
    - Conversores analógico para digital, para converter os sinais de sensores condicionados em valores digitais.
- Essa é a etapa mais custosa de todo o processo e exige o dimensionamento adequado desses aparelhos de aquisição, além da construção de um sistema de armazenamento dessa informação.


## <center>Formato dos Dados</center>

- São convertidos para representação binárias de seus elementos fundamentais, textos ou números e são dispostos em vetores/matrizes para o acesso do usuário.
    - Texto;
    - Imagem/Video;
    - Som;
    - Tabela


## <center>Classificação dos Dados</center>

- Os dados tabulares/vetores ainda são classificados de acordo com o tipo de entidade descrito e sua relação com outros dados. 

### Quantitativo VS Qualitativo 

- __Qualitativos__: Descrevem qualidades ou características.
    - Coletado por meio de questionários, entrevistas ou observação e frequentemente aparece na forma de narrativa.
    - Ex: Anotações feitas dutante um grupo de foco sobre a qualidade da comida no Cafe ou um questionário aberto.
    - Pode ser difícil de medir e analisar com precisão.
    - Pode estar na forma de palavras descritivas que podem ser examinadas quanto a padrões ou significado.

- __Quantitativos__: São usados quando está se tentando quantificar um problema ou abordar o "o quê" ou "quantos" aspectos de uma questão de pesquisa.
    - São dados que podem ser contados ou comparados em uma escala numérica.
    - São geralmente coletados por meio de instrumentos, como um questionário que inclui uma escala de classificação ou um termômetro para coletar dados meteorológicos.

### Nominal, Ordinal, Discreto e Contínuo

- __Nominal__: Conjunto de valores que não possuem uma ordem natural. Ex: A cor de um objeto.
- __Ordinal__: Valores que têm uma ordem natural, embora mantendo sua classe de valores. Ex: O sistema de classificação durante a classificação dos candidatos em um teste em que A+ é melhor do que a nota B.
- __Discreto__: Números inteiros são colocados nesta categoria. Ex: O número de alto-falantes no telefone, câmeras, núcleos no processador, o número de sims suportados
- __Contínuo__: Os números fracionários são considerados valores contínuos. Eles podem assumir a forma de frequência operacional dos processadores, a versão Android do telefone, frequência wi-fi, temperatura dos núcleos e assim por diante.

### Não dependente VS dependente

- __Dados orientados para não dependência__: Refere-se tipo de dados simples, como multi-dimensionais ou dados de textos.
    - Mais simples e mais comumente encontrados.
    - Registros de dados não possuem dependências especificadas entre os itens de dados ou os atributos.
    - Ex: Conjunto de daods demográficos com registros sobre indivíduos contendo sua idade, sexo e código postal.
- __Dados orientados a dependência__: Podem existir relacionamentos implícitos ou explícitos entre itens de dados.
    - Ex: Conjunto de dados de rede social contém um conjunto de vértices (itens de dados) que são conectados por um conjunto de arestas (relacionamentos).
    - Ex: Série temporeal contém dependências implícitas, como dois sucessivos valores coletados de um sensor provavelmente estão relacionados entre si.


## <center>Armazenamento dos Dados</center>

- São armazenados em diferentes formatos em algum local físico e podem ser acessados diretamente ou por meio de protocolos de conexão Web para o caso de armazenamento remoto.
    - Som: wav, mp3, ogg
    - Imagem: png, jpeg
    - Vídeo: mp4, mkv, avi
    - Texto: txt, docx, pdf
    - Tabela: csv, xlsx, parquet
    - Espacial: shp, kmv
    - Estatíco: dta, xport
    - Interchange: json, ubj

Geralmente são armazenados em um disco rígido, e pode estar em diferentes locais, no computador pessoal, em um servidor ou um Data Warehouse (conjunto de servidores conectados entre si) e esses dois últimos geralmente se comunica por meio de uma conexão web, que pode ser feita a partir de uma série de protocolos. Sendo eles: http/https, ftp, tcp/ip, imap, smtp ou udp. 


## <center>Aquisição de Dados</center>

- No contexto de mineração de daods, a aquisição corresponde ao processo de extração dos dados coletados para o sistema que fará a limpeza e processamento desses dados.

### Fontes Públicas
    - Nacionais:

        − https://www.gov.br/pt-br/orgaos-do-governo
        − https://ftp.ibge.gov.br/
        − https://geoftp.ibge.gov.br/
        − https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/inep-data
        − https://www.gov.br/anatel/pt-br/dados
        − https://dadosabertos.bcb.gov.br/

    - Internacionais:

        − http://data.worldbank.org/
        − https://ec.europa.eu/eurostat/en/web/lfs/statistics-illustrated
        − https://archive.org/web/

    - Empresas:

        − http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/
        − https://www.google.com/publicdata/directory?dl=pt_PT&hl=pt_PT
        − http://aws.amazon.com/public-data-sets/
        − https://webscope.sandbox.yahoo.com/catalog.php?datatype=r&did=75
        − https://www.kaggle.com/datasets

### Fontes Proprietárias
    - SQL Server
    - Oracle
    - Azure 

### API(aplication programming interface)
    - Google(https://developers.google.com/apis-explorer)
        − Geocoding (https://geopy.readthedocs.io/en/stable/)
        − Search (https://developers.google.com webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python)
    − Gmail (https://developers.google.com/gmail/api/quickstart/python)
    - Twitter (https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries)
    - Receita Federal (https://www.gov.br/conecta/catalogo/apis/consulta-cnpj/swagger_view)
    - Correios (https://pypi.org/project/pycep-correios/)
    - Bacen (https://dadosabertos.bcb.gov.br/dataset/sistema-de-registro-de-operacoes-de-credito-com-o-setor-publico-cadip)
    - Yahoo Finance (https://pypi.org/project/yfinance/)
    - Open Weather (https://rapidapi.com/blog/openweathermap-api-overview/python/)

### Web Scrapping 
    - https://docs.python.org/3/library/urllib.html
    - https://docs.python-requests.org/en/master/
    - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - https://selenium-python.readthedocs.io/