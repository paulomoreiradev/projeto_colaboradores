
# Projeto Colaboradores

O Projeto Colaboradores foi feito para um teste para uma vaga de estágio na empresa Smartflow Sistemas. O projeto é construído em duas partes, uma API que fornece um CRUD por meio de endpoints pelo qual o usuário pode inserir e modificar colaboradores dentro do sistema, e uma página web que permite fazer as mesmas alterações sem a necessidade de consumir uma API


* POST via Formulário (OK)
* Painel de Controle DELETE & PUT (Em desenvolvimento)
* Tabela apresentando todos os Colaboradores cadastrados (OK)


## Documentação da Aplicação

### Instalações necessárias
Para utilizar a aplicação é necesário instalar alguns recursos

#### Instalação do Python

Verifique se tem a versão 3.8.10 (ou superior) instalada em sua máquina.

### Criação e ativação do ambiente virtual

Crie um ambiente virtual de desenvolvimento por meio do comando

No Windows:
```http
python -m venv env
```
No Linux:
```http
python3 -m venv env
```

Após criar o ambiente virtual certifique-se de ativá-lo

No windows:

CMD:
```http
C:\> <venv>\Scripts\activate.bat
```

Power Shel:

```http
PS C:\> <venv>\Scripts\Activate.ps1
```

No Linux:

```http
source <venv>/bin/activate
```

### Instalações necessárias

```http
pip install -r requirements.txt
```

### Rodando o projeto

Após fazer as instalações necessárias, abra o Terminal no diretório que contém o arquivo 'manage.py' e rode o seguinte comando:

No windows:
```http
python .\manage.py runserver
```
No Linux

```http
python3 manage.py runserver
```

Após esses passos, a aplicação web ficará disponível via servidor local que pode ser aberto diretamente no browser preferido e API também ficara disponível na mesma porta.
## Informações complementares

Dentro da pasta 'recursos' você pode encontrar um arquivo 'colaboradores_api.postman_collection' que pode ser importado para o software Postman para conhecer melhor os endpoints fornecidos via API.

