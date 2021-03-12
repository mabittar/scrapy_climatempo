# scrapy_climatempo
Objetivo: obter a temperatura atual utilizando o scrapy, armazená-la em BD e automatizar o processo


## Requisitos

 [x] utilizar scrapy para obter informações do clima agora em uma cidade.

 [x] obter a temperatura no momento

    [x] obter umidade

    [x] sensação 

    [x] vento


 [x] atualizar o scrapy para obter informações do clima agora de X cidades.

 [] salvar os dados persistentemente.

 [x] realizar o deploy

 [x] obter informação de hora em hora


 ### Como desenvolver

  1. clone o repositório com `git clone https://github.com/mabittar/scrapy_climatempo`
  2. mova o caminho para o diretório do projeto `cd scrapy_climatempo`
  3. crie o venv com Python 3.6 ou superior `python -m venv .`
  4. ative o venv `.\Scritps\activate`
  5. instale as dependências utilizando `pip install -r requirements.txt`
  6. mova para o diretório do scrapy `cd ct`
  7. para obter os dados utilize o comando `scrapy crawl climatempo -o clima.csv` será criado um arquivo clima.csv com as informações obtidas.

  ## Como fazer o Deploy? 

  0. faça o cadstro em https://www.zyte.com/scrapy-cloud/
  1. faça o login com `shub login`
  2. será solicitado a chave API que pode ser obtida no painel do usuário após o login no site zyte.com
  3. 